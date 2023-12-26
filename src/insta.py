from instagrapi import Client
from src.config import INSTAGRAM_USERNAME, INSTAGRAM_PASSWORD


client = Client()
client.login(INSTAGRAM_USERNAME, INSTAGRAM_PASSWORD)
