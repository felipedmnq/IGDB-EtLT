from requests import Session
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry


class SessionHandler:
    def __init__(self) -> None:
        self.session = self.get_session()

    def __create_session(
        self,
        retries: int = 3,
        backoff_factor: float = 0.3,
        status_forcelist: tuple[int] = tuple(range(400, 430)) + (500, 502, 503, 504),
    ) -> Session:
        session = Session()

        retry = Retry(
            total=retries,
            read=retries,
            connect=retries,
            backoff_factor=backoff_factor,
            status_forcelist=status_forcelist,
            allowed_methods=("GET", "POST"),
        )

        session_adapter = HTTPAdapter(max_retries=retry)

        session.mount("http://", session_adapter)
        session.mount("https://", session_adapter)

        return session

    def get_session(self) -> Session:
        return self.__create_session()
