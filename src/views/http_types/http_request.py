class HttpRequest:
    def __init__(
        self,
        body: dict = None,
        headers: dict = None,
        params: dict = None,
        token_infos: dict = None
    ) -> None:

        self.__body = body
        self.__headers = headers
        self.__params = params
        self.__token_infos = token_infos


http_request = HttpRequest(body={"hello": "world"})
