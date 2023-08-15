import os
from dataclasses import dataclass


@dataclass
class IGDBConfigs:
    IGDB_CLIENT_ID: str = os.getenv("IGDB_CLIENT_ID")
    IGDB_CLIENT_SECRET: str = os.getenv("IGDB_CLIENT_SECRET")
    IGDB_TOKEN_URL: str = "https://id.twitch.tv/oauth2/token"
