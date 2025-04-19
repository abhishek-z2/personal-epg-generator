from epg.fetch_epg import fetch_epg
from utils.tor_utils import test_tor_connection
from epg.xmltv_export import epg_to_xmltv

if __name__ == "__main__":
    print("🔍 Checking Tor connection...")
    test_tor_connection()

    print("\n🌐 Fetching Pluto.tv homepage through Tor...")
    fetch_epg()
    data = fetch_epg()
    # print(f"type of response: {type(data)}")
    epg_to_xmltv(data)
