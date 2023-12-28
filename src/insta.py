import json

from instagrapi import Client
from src.config import INSTAGRAM_USERNAME, INSTAGRAM_PASSWORD, BASE_PATH

cookies = None

try:
    with open(f"{BASE_PATH}/assets/cookies.json") as file:
        cookies = json.load(file)
except FileNotFoundError:
    cookies = None

if cookies is None:
    client = Client()

    client.login(INSTAGRAM_USERNAME, INSTAGRAM_PASSWORD)

    with open(f"{BASE_PATH}/assets/cookies.json", "w") as file:
        json.dump(client.get_settings(), file, indent=4)
else:
    client = Client(cookies)
