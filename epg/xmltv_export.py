import xml.etree.ElementTree as ET
from datetime import datetime,timedelta

def format_channel_slug(slug: str) -> str:
    return slug.replace('-', ' ').upper()

def convert_to_ist(utc_str):
    dt_utc = datetime.strptime(utc_str, "%Y-%m-%dT%H:%M:%S.%fZ")
    dt_ist = dt_utc + timedelta(hours=5, minutes=30)
    return dt_ist.strftime("%Y%m%d%H%M%S") + " +0530"

def epg_to_xmltv(epg_data, output_file="pluto_epg.xml"):
    if not epg_data:
        print("epg data not found")
        return

    tv = ET.Element("tv")

    # Create a set to store unique channel IDs
    channel_ids = set()


    for channel in epg_data:
        channel_id = channel.get("channelId")
        channel_slug = channel.get("channelSlug", "Unknown Channel")
        
        if channel_id and channel_id not in channel_ids:
            channel_ids.add(channel_id)
            ch_el = ET.SubElement(tv, "channel", id=channel_id)
            dn_el = ET.SubElement(ch_el, "display-name")
            dn_el.text =  format_channel_slug(channel_slug)


    # Second pass: Create programme elements
    for channel in epg_data:
        channel_id = channel.get("channelId")
        for show in channel.get("timelines", []):
            if not channel_id:
                continue  # Skip if channel ID is missing

            start = show.get("start", "")
            stop = show.get("stop", "")
            title = show.get("title", "Untitled")

            # Format start and stop times to XMLTV format: YYYYMMDDHHMMSS +0000
            def format_time(t):
                try:
                    dt = datetime.strptime(t, "%Y-%m-%dT%H:%M:%S.%fZ")
                    return dt.strftime("%Y%m%d%H%M%S") + " +0000"
                except ValueError:
                    return ""

            start_formatted = format_time(start)
            stop_formatted = format_time(stop)

            prog_el = ET.SubElement(tv, "programme", start=start_formatted, stop=stop_formatted, channel=channel_id)
            title_el = ET.SubElement(prog_el, "title", lang="en")
            title_el.text = title

    tree = ET.ElementTree(tv)
    tree.write(output_file, encoding="utf-8", xml_declaration=True)
    print(f"✅ Wrote XMLTV file: {output_file}")



def epg_to_xmltv_ist(epg_data, output_file="pluto_epg_ist.xml"):
    if not epg_data:
        print("epg data not found")
        return

    tv = ET.Element("tv")

    # Create a set to store unique channel IDs
    channel_ids = set()


    for channel in epg_data:
        channel_id = channel.get("channelId")
        channel_slug = channel.get("channelSlug", "Unknown Channel")
        
        if channel_id and channel_id not in channel_ids:
            channel_ids.add(channel_id)
            ch_el = ET.SubElement(tv, "channel", id=channel_id)
            dn_el = ET.SubElement(ch_el, "display-name")
            dn_el.text =  format_channel_slug(channel_slug)


    # Second pass: Create programme elements
    for channel in epg_data:
        channel_id = channel.get("channelId")
        for show in channel.get("timelines", []):
            if not channel_id:
                continue  # Skip if channel ID is missing

            start = show.get("start", "")
            stop = show.get("stop", "")
            title = show.get("title", "Untitled")

            # Format start and stop times to XMLTV format: YYYYMMDDHHMMSS +0000
            # def format_time(t):
            #     try:
            #         dt = datetime.strptime(t, "%Y-%m-%dT%H:%M:%S.%fZ")
            #         return dt.strftime("%Y%m%d%H%M%S") + " +0000"
            #     except ValueError:
            #         return ""

            start_formatted = convert_to_ist(start)
            stop_formatted = convert_to_ist(stop)

            prog_el = ET.SubElement(tv, "programme", start=start_formatted, stop=stop_formatted, channel=channel_id)
            title_el = ET.SubElement(prog_el, "title", lang="en")
            title_el.text = title

    tree = ET.ElementTree(tv)
    tree.write(output_file, encoding="utf-8", xml_declaration=True)
    print(f"✅ Wrote XMLTV file: {output_file}")
