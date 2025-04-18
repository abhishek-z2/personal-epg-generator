from epg.fetch_epg import fetch_pluto_homepage
from utils.tor_utils import test_tor_connection

if __name__ == "__main__":
    print("🔍 Checking Tor connection...")
    test_tor_connection()

    print("\n🌐 Fetching Pluto.tv homepage through Tor...")
    fetch_pluto_homepage()
