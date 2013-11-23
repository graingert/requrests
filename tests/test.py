import requrests
from unittest import TestCase

from six.moves import http_server as server


class TestREST(object):
    def setUp(self):
        self.api = requrests.REST(
            "http://localhost:8000/index.json"
        )

    def test_ham(self):
        assert_equal(
            self.api["hams"][0]["description"],
            "It tastes good!"
        )

def setup_module():
    
