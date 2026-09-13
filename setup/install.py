import shutil
import ctypes
from ctypes import wintypes
from pathlib import Path
import json

BASE_DIR=Path().resolve()

def create_json_files():
    # creating lec_log.json
    lec_log_file_path=BASE_DIR.parent / "RevisionSystem" / "lec_log.json"
    # creating personalization.json
    personalization_file_path=BASE_DIR.parent / "RevisionSystem" / "revision_script" / "personalization.json"
    # creating revision_log.json
    revision_log_path=BASE_DIR.parent / "RevisionSystem" / "revision_script" / "revision_log.json"

    try:
        with open(lec_log_file_path, "w", encoding="utf-8") as lec_log_file:
            json.dump({}, lec_log_file)

        print(f"Successfully created lec_log.json file")

        with open(personalization_file_path, "w", encoding="utf-8") as personalization_file:
            json.dump({
    "revision_chapter_per_day": 1,
    "revision_interval_days": 1,
    "subject_in_planner": []}, personalization_file)

        print(f"Successfully created personalization.json file")

        with open(revision_log_path, "w", encoding="utf-8") as revision_file_path:
            json.dump({}, revision_file_path)

        print(f"Successfully created revision_log.json file")

    except Exception as e:
        print("Error occured!")



def get_desktop_path():
    CSIDL_DESKTOPDIRECTORY = 0x0010

    path = ctypes.create_unicode_buffer(wintypes.MAX_PATH)

    ctypes.windll.shell32.SHGetFolderPathW(
        None,
        CSIDL_DESKTOPDIRECTORY,
        None,
        0,
        path
    )

    return Path(path.value)


def create_revision_runner_file():

    bat_file = BASE_DIR.parent / "RevisionScheduler.bat"
    print(bat_file)

    bat_content = f'''@echo off
cd /d "{BASE_DIR.parent}"
call .venv\\Scripts\\activate.bat
python -m RevisionSystem.terminalIO
pause
'''

    # Create BAT at Tracker root
    bat_file.write_text(bat_content, encoding="utf-8")

    # Get actual Windows Desktop
    desktop = get_desktop_path()

    # Copy BAT to Desktop
    shutil.copy2(
        bat_file,
        desktop / bat_file.name
    )

def install():
    # creating all the json files
    print("Creating json files for data storage!")
    create_json_files()
    create_revision_runner_file()
    print("Created RevisionScheduler.bat file in root directory and desktop both just click to run the system.")



if __name__=="__main__":
    install()