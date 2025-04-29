import requests
import os
TOR_PORT = os.getenv("TOR_PORT", "9050")  # default to 9050 if not set

def get_tor_session():
    session = requests.Session()


    session.proxies = {
        'http': f'socks5h://127.0.0.1:{TOR_PORT}',
        'https': f'socks5h://127.0.0.1:{TOR_PORT}'
    }


    # session.proxies = {
    #     'http': 'socks5h://127.0.0.1:9050',
    #     'https': 'socks5h://127.0.0.1:9050'
    # }
    ipinfo = session.get("http://ip-api.com/json/").json()
    print(ipinfo)
    return session

def test_tor_connection():
    session = get_tor_session()
    try:
        response = session.get("https://check.torproject.org/", timeout=10)
        if "Congratulations" in response.text:
            print("✅ Successfully connected to Tor!")
        else:
            print("⚠️ Not using Tor.")
    except Exception as e:
        print("❌ Tor connection failed:", e)

if __name__ == "__main__":
    test_tor_connection()
