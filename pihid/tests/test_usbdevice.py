import sys
from nose.tools import assert_equal
sys.path.append("../../")
from pihid.USBDevice import Device
from pihid.USBRemote import Remote


class TestUSBDevice(object):
    def setUp(self):
        self.device = Device('serial123', 'main', 'testdevice')

    def test_init(self):
        dev = Device('serial123', 'main', 'testdevice')
        assert_equal(dev.serialnumber, 'serial123')
        assert_equal(dev.manufacturer, 'main')
        assert_equal(dev.product_name, 'testdevice')

    def test_default_cfg(self):
        assert_equal(self.device.configs[0].params['MaxPower'], 250)

    def test_should_add_remote_function(self):
        f = Remote()
        assert_equal(self.device.functions, {})
        self.device.add('remote', f)
        assert_equal(self.device.functions, {'remote': f})

    def test_should_set_report_id(self):
        f = Remote()
        self.device.add('remote', f)
        assert_equal(f.report_id, 1)
        f1 = Remote()
        self.device.add('remote1', f1)
        assert_equal(f1.report_id, 2)
