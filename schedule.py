import os

from src.config import BASE_PATH
from src.insta import client


def schedule():
    DAILY_PATH = f"{BASE_PATH}/assets/daily"
    files = os.listdir(DAILY_PATH)

    for file in files:
        media = client.video_upload(f"{DAILY_PATH}/{file}", "Happy birthday!")
