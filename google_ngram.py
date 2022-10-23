import requests
import typing
from dataclasses import dataclass

class Params:
    content: str
    
class GoogleNgram:
    """Google Ngram object for storing parameters and JSON output."""
    def __init__(self) -> None:
        self._url = "https://books.google.com/ngrams/json?"
        self.data: typing.Dict[str, typing.Any] = {}
        self.params: typing.Dict[str, typing.Any] = {}

    def set_param(self, param: str, value: str):
        if param == "content" and self.params.get("content",False):
            self.params[param] += f",{value}"
        else:
            self.params[param] = value

    def update_url(self) -> None:
        """Update the url with the latest parameters."""

        url = "https://books.google.com/ngrams/json?"

        for key, value in self.params.items():
            if url[-1] == "?":
                url = f"{url}{key}={value}"
            else:
                url = f"{url}&{key}={value}"
        self._url = url

    def _set_data(self, data: typing.Dict[str, typing.Any]) -> None:
        self.data = data

    def request_data(self) -> typing.Dict[str, typing.Any]:
        """Call data from the built URL. Raises exception if the request doesn't return any data."""
        self.update_url()
        
        response = requests.get(self._url)
        
        data = {}
        for ngram in response.json():
            word = ngram["ngram"]
            time_series = ngram["timeseries"]

            data[word] = time_series

        self._set_data(data)

        if not self.data:
            self._set_data({})
            raise Exception("The URL did not return any data.")
        return self.data

if __name__ == "__main__":
    test = GoogleNgram()
    test.set_param("content","Albert+Einstein")
    print(test._url, type(test.request_data()), test.request_data())