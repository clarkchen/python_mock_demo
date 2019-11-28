from pprint import pprint

from src.req import do_request
import requests

def get_baidu():
    url = "http://www.baidu.com"
    ret = do_request(url)
    pprint(ret)
    return ret

def get_baidu_from_requests():
    url = "http://www.baidu.com"
    ret = requests.get(url)
    pprint(ret)
    return ret