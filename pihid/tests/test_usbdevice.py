import sys
from nose.tools import assert_equal
sys.path.append("../../")
from pihid.USBDevice import Device


class TestUSBDevice(object):
    def setUp(self):
        self.device = Device('serial123', 'main', 'testdevice')

    def test_init(self):
        dev = Device('serial123', 'main', 'testdevice')
        assert_equal(dev.serial_number, 'serial123')
        assert_equal(dev.manufacturer, 'main')
        assert_equal(dev.product_name, 'testdevice')

    def test_default_cfg(self):
        assert_equal(self.device.configs[0].params['MaxPower'], 250)
