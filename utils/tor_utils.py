import requests

def get_tor_session():
    session = requests.Session()
    session.proxies = {
        'http': 'socks5h://127.0.0.1:9050',
        'https': 'socks5h://127.0.0.1:9050'
    }
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
