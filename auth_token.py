import requests
import os

def get_pluto_auth_token():
    url = "https://boot.pluto.tv/v4/start"
    params = {
        "appName": "web",
        "appVersion": "9.11.0-fd026e7e9714f1e273c3c58069eb9e967f2c7ca8",
        "deviceVersion": "128.0.0",
        "deviceModel": "web",
        "deviceMake": "firefox",
        "deviceType": "web",
        "clientID": "196afddd-979a-46b8-b248-34100e5e0b74",
        "clientModelNumber": "1.0.0",
        "channelID": "62ba60f059624e000781c436",
        "serverSideAds": "false",
        "blockingMode": "",
        "notificationVersion": "1",
        "appLaunchCount": "0",
        "lastAppLaunchDate": "2025-04-23T18%3A38%3A28.305Z",
        "clientTime": "2025-04-23T18%3A44%3A17.845Z",
    }

    response = requests.get(url, params=params)
    response.raise_for_status()
    
    # Retrieve sessionToken
    session_token = response.json().get("sessionToken")
    if not session_token:
        raise Exception("No sessionToken found in the response.")
    
    return session_token

def save_token():
    token = get_pluto_auth_token()
    with open("token.txt", "w") as f:
        f.write(token)
    print("Token saved successfully.")

if __name__ == "__main__":
    save_token()
