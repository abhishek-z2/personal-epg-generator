import requests
from datetime import datetime
import uuid

def get_pluto_session_token(session):
    now = datetime.utcnow().isoformat(timespec='milliseconds') + 'Z'
    
    params = {
        "appName": "web",
        "appVersion": "9.11.0-fd026e7e9714f1e273c3c58069eb9e967f2c7ca8",
        "deviceVersion": "128.0.0",
        "deviceModel": "web",
        "deviceMake": "firefox",
        "deviceType": "web",
        "clientID": str(uuid.uuid4()),
        "clientModelNumber": "1.0.0",
        "channelID": "5f4d8594eb979c0007706de7",  
        "serverSideAds": "false",
        "blockingMode": "",
        "notificationVersion": "1",
        "appLaunchCount": "0",
        "lastAppLaunchDate": now,
        "clientTime": now,
    }

    headers = {
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate, br, zstd",
        "Accept-Language": "en-US,en;q=0.5",
        "Cache-Control": "no-cache",
        "Connection": "keep-alive",
        "Host": "boot.pluto.tv",
        "Origin": "https://pluto.tv",
        "Pragma": "no-cache",
        "Referer": "https://pluto.tv/",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-site",
        "Sec-GPC": "1",
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0"
    }

    response = session.get("https://boot.pluto.tv/v4/start", params=params, headers=headers)


    if response.status_code == 200:
        print(response.text)
        data = response.json()
        return data.get("sessionToken")
    else:
        print(f"Failed to get token. Status code: {response.status_code}")
        return None
# print()
# print(get_pluto_session_token())