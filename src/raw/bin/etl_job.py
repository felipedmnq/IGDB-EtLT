from src.configs.configs import IGDBConfigs as Configs
from src.raw.libs.igdb_api import get_token
from src.raw.libs.session_handler import SessionHandler


def main():
    session = SessionHandler().get_session()
    token = get_token(Configs.IGDB_CLIENT_ID, Configs.IGDB_CLIENT_SECRET, session)
    print(f"\033[92mToken: {token}\033[0m")


if __name__ == "__main__":
    main()
