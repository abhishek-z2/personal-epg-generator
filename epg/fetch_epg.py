# from utils.tor_utils import get_tor_session
# from bs4 import BeautifulSoup

# def fetch_pluto_homepage():
#     session = get_tor_session()
#     url = "https://pluto.tv"

#     try:
#         response = session.get(url, timeout=10)
#         print(f"Status code: {response.status_code}")

#         # Parse the HTML safely
#         soup = BeautifulSoup(response.text, "html.parser")
#         title = soup.title.string.strip() if soup.title else "No <title> tag found"
#         print("✅ Page title:", title)
#     except Exception as e:
#         print("❌ Error fetching Pluto TV:", e)


from utils.tor_utils import get_tor_session
from datetime import datetime, timedelta
import requests
import json
import logging

start_time = (datetime.utcnow() - timedelta(minutes=10)).isoformat(timespec="seconds") + ".000Z"
logging.basicConfig(level=logging.INFO)

def fetch_epg():
    # session = get_tor_session()
    session = requests.Session()

    url = "https://service-channels.clusters.pluto.tv/v2/guide/timelines"
    params = {
        "start": start_time,
        "duration": "240"
    }
    headers = {

        "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsImtpZCI6IjQ1MDJhY2VjLTVhNTEtNDhiZS1iYjM3LWVlODlmMWFhZDNlZiIsInR5cCI6IkpXVCJ9.eyJzZXNzaW9uSUQiOiI1NzlhMDZmMS0xY2Q1LTExZjAtOTFjOS03YTQyOTViNTM0MzkiLCJjbGllbnRJUCI6IjI2MDQ6MmRjMDoxMDE6MjAwOjo1M2M4IiwiY2l0eSI6IlJlc3RvbiIsInBvc3RhbENvZGUiOiIyMDE5MCIsImNvdW50cnkiOiJVUyIsImRtYSI6NTExLCJhY3RpdmVSZWdpb24iOiJVUyIsImRldmljZUxhdCI6MzguOTU5OTk5MDg0NDcyNjU2LCJkZXZpY2VMb24iOi03Ny4zMzk5OTYzMzc4OTA2MiwicHJlZmVycmVkTGFuZ3VhZ2UiOiJlbiIsImRldmljZVR5cGUiOiJ3ZWIiLCJkZXZpY2VWZXJzaW9uIjoiMTI4LjAuMCIsImRldmljZU1ha2UiOiJmaXJlZm94IiwiZGV2aWNlTW9kZWwiOiJ3ZWIiLCJhcHBOYW1lIjoid2ViIiwiYXBwVmVyc2lvbiI6IjkuMTEuMC1mZDAyNmU3ZTk3MTRmMWUyNzNjM2M1ODA2OWViOWU5NjdmMmM3Y2E4IiwiY2xpZW50SUQiOiIzYTUzM2QwOS0xYjY0LTQ4ZjgtOTQyMi1iMjIzOTMyNzBlN2EiLCJjbUF1ZGllbmNlSUQiOiIiLCJpc0NsaWVudEROVCI6ZmFsc2UsInVzZXJJRCI6IiIsImxvZ0xldmVsIjoiREVGQVVMVCIsInRpbWVab25lIjoiQW1lcmljYS9OZXdfWW9yayIsInNlcnZlclNpZGVBZHMiOmZhbHNlLCJlMmVCZWFjb25zIjpmYWxzZSwiZmVhdHVyZXMiOnsiYWRMb2FkIjp7ImNvaG9ydCI6IiJ9LCJtdWx0aUF1ZGlvIjp7ImVuYWJsZWQiOnRydWV9LCJtdWx0aVBvZEFkcyI6eyJlbmFibGVkIjp0cnVlfSwic2VhcmNoQVBJIjp7Im1hdGNoRXhhY3RJblBocmFzZUVuYWJsZWQiOnRydWUsIm1hdGNoSW5BY3RvcnNCb29zdCI6MjUsIm1hdGNoSW5BY3RvcnNFZGl0RGlzdGFuY2UiOiJBVVRPOjUsMTEiLCJtYXRjaEluQWN0b3JzRW5hYmxlZCI6dHJ1ZSwibWF0Y2hJbkRpcmVjdG9yc0Jvb3N0IjoyNSwibWF0Y2hJbkRpcmVjdG9yc0VkaXREaXN0YW5jZSI6IkFVVE86NSwxMSIsIm1hdGNoSW5EaXJlY3RvcnNFbmFibGVkIjp0cnVlLCJuZXh1c1RpbWVvdXRNcyI6NTAwLCJxdWVyeVN5bm9ueW1zRW5hYmxlZCI6dHJ1ZSwicXVlcnlWZXJzaW9uIjoiaHlicmlkIiwic2VhcmNoUHJveHlFbmhhbmNlbWVudCI6ZmFsc2V9fSwiZm1zUGFyYW1zIjp7ImZ3VmNJRDIiOiIzYTUzM2QwOS0xYjY0LTQ4ZjgtOTQyMi1iMjIzOTMyNzBlN2EiLCJmd1ZjSUQyQ29wcGEiOiIzYTUzM2QwOS0xYjY0LTQ4ZjgtOTQyMi1iMjIzOTMyNzBlN2EiLCJjdXN0b21QYXJhbXMiOnsiZm1zX2xpdmVyYW1wX2lkbCI6IiIsImZtc19lbWFpbGhhc2giOiIiLCJmbXNfc3Vic2NyaWJlcmlkIjoiIiwiZm1zX2lmYSI6IiIsImZtc19pZGZ2IjoiIiwiZm1zX3VzZXJpZCI6IjNhNTMzZDA5LTFiNjQtNDhmOC05NDIyLWIyMjM5MzI3MGU3YSIsImZtc192Y2lkMnR5cGUiOiJ1c2VyaWQiLCJmbXNfcmFtcF9pZCI6IiIsImZtc19oaF9yYW1wX2lkIjoiIiwiZm1zX2JpZGlkdHlwZSI6IiIsIl9md18zUF9VSUQiOiIiLCJmbXNfcnVsZWlkIjoiMTAwMDAsMTAwMDkifX0sImlzcyI6ImJvb3QucGx1dG8udHYiLCJzdWIiOiJwcmk6djE6cGx1dG86ZGV2aWNlczpVUzpNMkUxTXpOa01Ea3RNV0kyTkMwME9HWTRMVGswTWpJdFlqSXlNemt6TWpjd1pUZGgiLCJhdWQiOiIqLnBsdXRvLnR2IiwiZXhwIjoxNzQ1MTIyNzA3LCJpYXQiOjE3NDUwMzYzMDcsImp0aSI6ImViNWM5NGUxLTE1NWEtNGMzYy1hNWY4LTExZGIyZDVmNDBiZSJ9.oiJ1lb-RGYDGokpzDiaJ2252wjjC_Mc8voj0WBFZDNE",  
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
