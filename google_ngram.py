import requests
from typing import List, Dict, Union, Literal, Any


class NoResultsError(BaseException):
    """Error for content that does not have any results in Google Ngram."""
    def __init__(self, content: str):
        self.content = content

    def __str__(self):
        return f"There are no results for the url {self.content}"
class Request:

    def __init__(self):
        self.query_strings: Dict[str, Any] = {
        "start_year": None,
        "end_year": None,
        "corpus": None,
        "case_insensitive": None,
        "smoothing": None
        }
    
    QUERYSTRINGS = ["start_year", "end_year", "corpus", "case_insensitive", "smoothing"]
    
    def set_parameter(self, parameter: Literal["start_year", "end_year", "corpus", "case_insensitive", "smoothing"], value) -> None:
        """Set the query string in the object for any request calls."""
        if parameter in self.QUERYSTRINGS:
            self.query_strings[parameter] = value
        else:
            raise AttributeError()

    def _construct_url(self, content: str):
        BASE_URL = "https://books.google.com/ngrams/json?"

        content_str: str = "content=" + str(content).replace(" ","+")
        url = BASE_URL + f"{content_str}"

        for attribute, value in self.query_strings.items():
            if value:
                url += f"&{attribute}={value}"

        return url

    def request_one(self, content: str="") -> List[Dict[str, Union[str, List[float]]]]:
        """Makes a request to the Google Ngram Viewer 'api' and returns the JSON response."""
        
        if not isinstance(content, str):
            raise TypeError(f"Request expects a string argument but got {type(content)}.")
        
        url = self._construct_url(content=content)

        output = requests.get(url).json()
        if not output:
            raise NoResultsError(url)

        return output