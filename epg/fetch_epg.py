from utils.tor_utils import get_tor_session
from datetime import datetime, timedelta
import json
import logging

start_time = (datetime.utcnow() - timedelta(minutes=10)).isoformat(timespec="seconds") + ".000Z"
logging.basicConfig(level=logging.INFO)

def fetch_epg(session,token):

    url = "https://service-channels.clusters.pluto.tv/v2/guide/timelines"
    params = {
        "start": start_time,
        "duration": "720"
    }
    headers = {

        "Authorization": f"Bearer {token}",  
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0",
        "Origin": "https://pluto.tv",
        "Referer": "https://pluto.tv/",
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate, br, zstd",
        "Accept-Language": "en-US,en;q=0.5",
        "Connection": "keep-alive"
    }

    try:
        print("📡 Fetching EPG data from Pluto TV...")
        response = session.get(url, params=params,headers=headers, timeout=15)
        response.raise_for_status()

        print(response.headers)
        # print("Request URL:", response.url)
        data = response.json()
        with open("epg_data.json", "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        # print(data)
        logging.info(f"Fetching EPG data for {len(data.get('data', []))} channels.")
        # print(data)
        print(f"✅ Fetched EPG data for {len(data.get('data',[]))} channels.\n")

        # Show a brief summary
        # for channel in data.get("data",[])[:3]:  # show only 3 for brevity
        #     name = channel.get("name", "Unknown Channel")
        #     shows = channel.get("timelines", [])
        #     print(f"📺 {name} ({len(shows)} shows):")
        #     for show in shows[:2]:
        #         title = show.get("title", "Untitled")
        #         start = show.get("start")
        #         end = show.get("stop")
        #         description = show.get("episode").get("description", "No description available")
        #         genre = show.get("genre", "Unknown genre")
        #         print(f"  - {title} ({start} to {end}) - {description} - {genre}")

        #     print()

        return(data.get("data",[]))
    except Exception as e:
        print(f"❌ Failed to fetch EPG: {e}")
        return None
