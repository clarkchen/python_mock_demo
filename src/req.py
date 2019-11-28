
import requests
def do_request(url):
    return requests.get(url).text