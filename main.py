from epg.fetch_epg import fetch_epg
from epg.xmltv_export import epg_to_xmltv, epg_to_xmltv_ist
import subprocess

if __name__ == "__main__":
    data = fetch_epg()
    epg_to_xmltv(data)
    epg_to_xmltv_ist(data)

    try:
        subprocess.run(["git", "add", "pluto_epg.xml", "pluto_epg_ist.xml"], check=True)
        subprocess.run(["git", "commit", "-m", "🔄 Auto update EPG XML files"], check=True)
        subprocess.run(["git", "push"], check=True)
        print("✅ Git push complete.")
    except subprocess.CalledProcessError as e:
        print("❌ Git error:", e)
