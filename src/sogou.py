from pprint import pprint

from src.req import do_request


def get_sougou():
    url = "http://www.sogou.com"
    ret = do_request(url)
    pprint(ret)
    return ret
