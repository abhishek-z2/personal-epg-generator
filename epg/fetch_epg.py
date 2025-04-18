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

def fetch_epg():
    session = get_tor_session()

    url = "https://service-channels.clusters.pluto.tv/v2/guide/timelines"
    params = {
        "start": "2025-04-18T05:30:00.000Z",
        "channelIds": (
            "66a244d5cd0d3100083b1e47,622f487722d9d400075f74dd,67a324d221af380008105d6f,"
            "609539fa709d6b0007b19887,66c6fc06489bab0008b6f9da,6683f7fe36a2f9000804940c,"
            "66c6fb43489bab0008b6f7cd,66337ed7a0a74e0008895699,60c716084d842c00085f6e64,"
            "622f40c901d4b70007ad7609,655ca57e4261ca00080b3a04,67a324d221af380008105d6f,"
            "609539fa709d6b0007b19887,66c6fc06489bab0008b6f9da,622f40c901d4b70007ad7609,"
            "622f6faf65be650007f57aab,667d63d236a2f90008f72269,655ca57e4261ca00080b3a04,"
            "630348a54c48ce00077eb6c7,622f6e1e2792150007e0b2ff,62cebf042ffc6d0007c4e59a"
        ),
        "duration": "240"
    }

    headers = {

        "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsImtpZCI6ImFhZGI2MzNhLTMyZjUtNGVlZS1iNjNkLTgxYTUwNWY0MDIxOCIsInR5cCI6IkpXVCJ9.eyJzZXNzaW9uSUQiOiIwOGRiZTEzYy0xYzIyLTExZjAtYWRlYi1hNjllNzlkMzJmMTAiLCJjbGllbnRJUCI6IjJhMGM6NTcwMDozMTMzOjE3MDU6YmUyNDoxMWZmOmZlZjU6N2MzOSIsImNpdHkiOiJHb3RlYm9yZyIsInBvc3RhbENvZGUiOiI0MTYgNDgiLCJjb3VudHJ5IjoiU0UiLCJkbWEiOjc1MjAwMiwiYWN0aXZlUmVnaW9uIjoiU0UiLCJkZXZpY2VMYXQiOjU3LjcwOTk5OTA4NDQ3MjY1NiwiZGV2aWNlTG9uIjoxMS45ODk5OTk3NzExMTgxNjQsInByZWZlcnJlZExhbmd1YWdlIjoiZW4iLCJkZXZpY2VUeXBlIjoid2ViIiwiZGV2aWNlVmVyc2lvbiI6IjEyOC4wLjAiLCJkZXZpY2VNYWtlIjoiZmlyZWZveCIsImRldmljZU1vZGVsIjoid2ViIiwiYXBwTmFtZSI6IndlYiIsImFwcFZlcnNpb24iOiI5LjExLjAtZmQwMjZlN2U5NzE0ZjFlMjczYzNjNTgwNjllYjllOTY3ZjJjN2NhOCIsImNsaWVudElEIjoiMzhiMGZiNjEtOTA4Zi00ZGViLWFjYTItODNjNmRlZjIzYjFmIiwiY21BdWRpZW5jZUlEIjoiIiwiaXNDbGllbnRETlQiOmZhbHNlLCJ1c2VySUQiOiIiLCJsb2dMZXZlbCI6IkRFRkFVTFQiLCJ0aW1lWm9uZSI6IkV1cm9wZS9TdG9ja2hvbG0iLCJzZXJ2ZXJTaWRlQWRzIjpmYWxzZSwiZTJlQmVhY29ucyI6ZmFsc2UsImZlYXR1cmVzIjp7Im11bHRpUG9kQWRzIjp7ImVuYWJsZWQiOnRydWV9fSwiZm1zUGFyYW1zIjp7ImZ3VmNJRDIiOiIzOGIwZmI2MS05MDhmLTRkZWItYWNhMi04M2M2ZGVmMjNiMWYiLCJmd1ZjSUQyQ29wcGEiOiIzOGIwZmI2MS05MDhmLTRkZWItYWNhMi04M2M2ZGVmMjNiMWYiLCJjdXN0b21QYXJhbXMiOnsiZm1zX2xpdmVyYW1wX2lkbCI6IiIsImZtc19lbWFpbGhhc2giOiIiLCJmbXNfc3Vic2NyaWJlcmlkIjoiIiwiZm1zX2lmYSI6IiIsImZtc19pZGZ2IjoiIiwiZm1zX3VzZXJpZCI6IjM4YjBmYjYxLTkwOGYtNGRlYi1hY2EyLTgzYzZkZWYyM2IxZiIsImZtc192Y2lkMnR5cGUiOiJ1c2VyaWQiLCJmbXNfcmFtcF9pZCI6IiIsImZtc19oaF9yYW1wX2lkIjoiIiwiZm1zX2JpZGlkdHlwZSI6IiIsIl9md18zUF9VSUQiOiIiLCJmbXNfcnVsZWlkIjoiMTAwMjAsMTAwMjEsMTAwMDksMTAwMTQsMTAwMTMsMTAwMTUsMTAwMTYsMTAwMDAsMTAwMDMifX0sImlzcyI6ImJvb3QucGx1dG8udHYiLCJzdWIiOiJwcmk6djE6cGx1dG86ZGV2aWNlczpTRTpNemhpTUdaaU5qRXRPVEE0WmkwMFpHVmlMV0ZqWVRJdE9ETmpObVJsWmpJellqRm0iLCJhdWQiOiIqLnBsdXRvLnR2IiwiZXhwIjoxNzQ1MDQ1Njk1LCJpYXQiOjE3NDQ5NTkyOTUsImp0aSI6IjFmMDZiYjNiLTBlNjMtNDc1Mi1hODFmLTU4ZjA0ODNmYzlhOCJ9.7lKwcEJPh4UTw78YS0Aww8PWC5Qls39z3p2mNYGMXZY",  
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

        data = response.json()
        print(data)
        print(f"✅ Fetched EPG data for {len(data)} channels.\n")

        # Show a brief summary
        for channel in data[:3]:  # show only 3 for brevity
            name = channel.get("name", "Unknown Channel")
            shows = channel.get("timelines", [])
            print(f"📺 {name} ({len(shows)} shows):")
            for show in shows[:2]:
                title = show.get("title", "Untitled")
                start = show.get("start")
                end = show.get("stop")
                print(f"  - {title} ({start} to {end})")
            print()

    except Exception as e:
        print(f"❌ Failed to fetch EPG: {e}")

if __name__ == "__main__":
    fetch_epg()
