from utils.tor_utils import get_tor_session
from bs4 import BeautifulSoup

def fetch_pluto_homepage():
    session = get_tor_session()
    url = "https://pluto.tv"

    try:
        response = session.get(url, timeout=10)
        print(f"Status code: {response.status_code}")

        # Parse the HTML safely
        soup = BeautifulSoup(response.text, "html.parser")
        title = soup.title.string.strip() if soup.title else "No <title> tag found"
        print("✅ Page title:", title)
    except Exception as e:
        print("❌ Error fetching Pluto TV:", e)
