import requests
from typing import List, Dict, Union


class NoResultsError(BaseException):
    """Error for content that does not have any results in Google Ngram."""
    def __init__(self, content: str):
        self.content = content

    def __str__(self):
        return f"There are no results for the string {self.content}"

def request(content: Union[str, List[str]]="", start_year: int=1800, end_year: int=2019, corpus: str="English (2019)", case_insensitve: bool=False, smoothing: int=3) -> List[Dict[str, Union[str, List[float]]]]:
    """Makes a request to the Google Ngram Viewer 'api' and returns the JSON response."""
    BASE_URL = "https://books.google.com/ngrams/json?"
    
    content_str: str = "content="

    # Handle cases for list or string.
    if isinstance(content, list):
        content_str += "%2C".join(content)
    else:
        content_str += content

    url = BASE_URL + f"{content_str}"
    output = requests.get(url).json()
    if not output:
        raise NoResultsError(content_str)

    return output