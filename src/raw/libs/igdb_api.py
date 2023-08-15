from requests import Session

from src.configs.configs import IGDBConfigs as Configs


def get_token(client_secret: str, client_id: str, session: Session) -> str:
    print(f"\033[091mGetting token for {client_id}\033[0m")
    params = {
        "client_id": client_id,
        "client_secret": client_secret,
        "grant_type": "client_credentials",
    }

    url = Configs.IGDB_TOKEN_URL
    response = session.post(url, params=params).json()

    return response["access_token"]
