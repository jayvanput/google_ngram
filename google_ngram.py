import requests
import typing

class GoogleNgram:

    def __init__(self) -> None:
        self.url = ""
        self.data: typing.Dict[str, typing.Any] = {}
        self.params: typing.Dict[str, str] = {}

    def _set_data(self, data: typing.Dict[str, typing.Any]) -> None:
        self.data = data

    def get_data(self) -> typing.Dict[str, typing.Any]:
        return self.data

    def request_data(self, url: str) -> typing.Dict[str, typing.Any]:
        response = requests.get(url)
        self._set_data(response.json()[0])

        return self.data


    def set_params(self):
        pass

if __name__ == "__main__":
    test = GoogleNgram()
    print(type(test.get_data()), test.get_data())