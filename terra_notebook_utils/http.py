import requests
from functools import lru_cache
from typing import BinaryIO

from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry


def set_retry(retry=None) -> requests.Session:
    session = requests.Session()
    retry = retry or Retry(total=10,
                           status_forcelist=[429, 500, 502, 503, 504],
                           method_whitelist=["HEAD", "GET"])
    adapter = HTTPAdapter(max_retries=retry)
    session.mount("https://", adapter)
    session.mount("http://", adapter)
    return session

http = set_retry()
