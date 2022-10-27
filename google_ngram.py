import json
import requests
from typing import List, Dict, Union
from dataclasses import dataclass

    

def request(content: Union[str, List[str]]="Albert Einstein", start_year: int=1800, end_year: int=2019, corpus: str="English (2019)", case_insensitve: bool=False, smoothing: int=3) -> List[Dict[str, Union[str, List[float]]]]:
    """Makes a request to the Google Ngram Viewer 'api' and returns the JSON response."""
    BASE_URL = "https://books.google.com/ngrams/json?"
    
    content_str: str = "content="
    if isinstance(content, list):
        content_str += "%2C".join(content)
    else:
        content_str += content

    url = BASE_URL + f"{content_str}"
    output = requests.get(url).json()
    print(type(output))
    return output