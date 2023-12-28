import os
import json

from src.config import BASE_PATH

from src.insta import client


def daily():
    DAILY_PATH = f"{BASE_PATH}/assets/daily"
    videos = os.listdir(DAILY_PATH)

    try:
        with open(f"{BASE_PATH}/assets/details.json") as file:
            details = json.load(file)

    except FileNotFoundError:
        with open(f"{BASE_PATH}/assets/details.json", "w") as file:
            file.write("{}")

        details = {}

    for video in videos:
        if video == ".gitignore" or ".jpg" in video:
            continue

        if video in details:
            caption = details[video]["caption"]
            counter = details[video]["counter"]
            details[video]["counter"] += 1
        else:
            caption = video
            counter = 1
            details[video] = {"caption": video, "counter": 2}

        caption += f"\nDay: {counter}"

        client.video_upload(
            f"{DAILY_PATH}/{video}", caption=caption.replace(".mp4", "")
        )

        print(f"The {video} is uploaded!")

    with open(f"{BASE_PATH}/assets/details.json", "w") as file:
        file.write(json.dumps(details, indent=4))


daily()
