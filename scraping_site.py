import requests
from bs4 import BeautifulSoup
import json


def get_ld_json(url: str) -> dict:
    parser = 'html.parser'
    req = requests.get(url)
    soup = BeautifulSoup(req.text, parser)
    return json.loads("".join(soup.find('script', type="application/ld+json").contents))


def find_name(url):
    json_file = get_ld_json(url)
    return json_file['name']
