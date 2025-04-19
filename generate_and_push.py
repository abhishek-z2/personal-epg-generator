import os
import shutil
import subprocess

def update_epg_repo(xml_path="pluto_epg.xml"):
    # Setup
    TEMP_DIR = "temp_epg_repo"
    REPO_URL = "https://github.com/yourusername/epg_ist.git"

    # Clean up if exists
    if os.path.exists(TEMP_DIR):
        shutil.rmtree(TEMP_DIR)

    # Clone the repo
    subprocess.run(["git", "clone", REPO_URL, TEMP_DIR])

    # Copy XML file to repo root or 'docs/'
    shutil.copy(xml_path, os.path.join(TEMP_DIR, "pluto_epg.xml"))

    # Commit and push
    subprocess.run(["git", "add", "pluto_epg.xml"], cwd=TEMP_DIR)
    subprocess.run(["git", "commit", "-m", "🔁 auto: update epg"], cwd=TEMP_DIR)
    subprocess.run(["git", "push"], cwd=TEMP_DIR)

    print("✅ EPG pushed to epg_ist repo")
