from unittest import TestCase, mock

from src.baidu import get_baidu, get_baidu_from_requests
from src.sogou import get_sougou


class TestGet(TestCase):
    def test_get_baidu(self):
        get_baidu()

    @mock.patch("src.baidu.do_request")
    def test_get_baidu(self, mock_req):
        mock_value = "mock value baidu"
        mock_req.return_value = mock_value
        ret = get_baidu()
        self.assertTrue(ret == mock_value)

    @mock.patch("src.baidu.requests.get")
    def test_get_baidu_by_requests(self, mock_req):
        mock_value = "mock value baidu requests"
        mock_req.return_value = mock_value
        ret = get_baidu_from_requests()
        self.assertTrue(ret == mock_value)

    @mock.patch("src.baidu.do_request")
    def test_get_baidu_mock_call_sougou(self, mock_req):
        mock_value = "mock value"
        mock_req.return_value = mock_value
        ret = get_baidu()
        print("\n"*3)
        self.assertTrue(ret == mock_value)
        ret_sogou = get_sougou()
        self.assertTrue(ret_sogou != mock_value)
