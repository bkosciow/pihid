import sys
from nose.tools import assert_equal
sys.path.append("../../")
from pihid.USBConfig import Config


class TestUSBDevice(object):
    def test_init(self):
        cfg = Config()
        assert_equal(cfg.params, {})
