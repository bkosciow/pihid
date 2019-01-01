import sys
from nose.tools import assert_equal
sys.path.append("../../")
from pihid.USBDevice import Device
from pihid.USBInstaller import Installer
from unittest.mock import MagicMock
from unittest.mock import call
from pihid.USBRemote import Remote


class TestUSBInstall(object):
    def setUp(self):
        self.device = Device('serial123', 'main', 'testdevice')
        self.installer = Installer(self.device)

    def test_init(self):
        dev = Device('serial123', 'main', 'testdevice')
        ins = Installer(dev)
        assert_equal(ins.device, dev)

    def test_install_should_call_subfunctions(self):
        self.device.path = "/a"
        self.installer._create_dirs = MagicMock()
        self.installer._create_files = MagicMock()
        self.installer._create_functions = MagicMock()
        self.installer._create_configs = MagicMock()
        self.installer._enable = MagicMock()

        self.installer.install()

        self.installer._create_dirs.assert_called_with()
        self.installer._create_files.assert_called_with()
        self.installer._create_functions.assert_called_with()
        self.installer._create_configs.assert_called_with()
        self.installer._enable.assert_called_with()

    def test_dirs_should_be_created(self):
        def always_false(a):
            return False
        self.device.path = "/a"
        self.device.lang = "0x101"
        self.installer._create_dir = MagicMock()
        self.installer._dir_exists = MagicMock()
        self.installer._dir_exists.side_effect = always_false

        self.installer._create_dirs()
        self.installer._create_dir.assert_has_calls([
            call("/a"),
            call("/a/strings/0x101"),
            call("/a/configs/c.1/strings/0x101"),
            call("/a/functions/hid.usb0")
        ])

    def test_files_should_be_created(self):
        self.device.path = "/a"
        self.installer._fileputcontent = MagicMock()
        self.installer._create_files()
        self.installer._fileputcontent.assert_has_calls([
            call("/a/idVendor", "0x1d6b"),
            call("/a/idProduct", "0x0104"),
            call("/a/bcdDevice", "0x0100"),
            call("/a/bcdUSB", "0x0200"),
            call("/a/strings/0x409/serialnumber", "serial123"),
            call("/a/strings/0x409/manufacturer", "main"),
            call("/a/strings/0x409/product", "testdevice")
        ])

    def test_configs_should_be_created(self):
        self.device.path = "/a"
        self.installer._fileputcontent = MagicMock()
        self.installer._create_configs()
        self.installer._fileputcontent.assert_has_calls([
            call("/a/configs/c.1/MaxPower", "250")
        ])

    def test_should_install_remote_descriptor(self):
        self.device.path = "/a"
        self.installer._create_symlink = MagicMock()
        f = Remote()
        self.device.add('remote', f)
        f1 = Remote()
        self.device.add('remote1', f1)
        self.installer._fileputcontent = MagicMock()
        self.installer._create_functions()
        self.installer._fileputcontent.assert_has_calls([
            call("/a/functions/hid.usb0/report_desc", [5, 12, 9, 1, 161, 1, 133, 1, 21, 0, 37, 1, 9, 233, 9, 234, 117, 1, 149, 2, 129, 6, 9, 226, 149, 1, 129, 6, 9, 176, 149, 1, 129, 6, 9, 177, 149, 1, 129, 6, 9, 183, 149, 1, 129, 6, 9, 181, 149, 1, 129, 6, 9, 182, 149, 1, 129, 6, 9, 179, 149, 1, 129, 6, 9, 180, 149, 1, 129, 6, 149, 6, 129, 7, 192, 5, 12, 9, 1, 161, 1, 133, 2, 21, 0, 37, 1, 9, 233, 9, 234, 117, 1, 149, 2, 129, 6, 9, 226, 149, 1, 129, 6, 9, 176, 149, 1, 129, 6, 9, 177, 149, 1, 129, 6, 9, 183, 149, 1, 129, 6, 9, 181, 149, 1, 129, 6, 9, 182, 149, 1, 129, 6, 9, 179, 149, 1, 129, 6, 9, 180, 149, 1, 129, 6, 149, 6, 129, 7, 192], "wb"),
            call("/a/functions/hid.usb0/report_length", "8")
        ])
        self.installer._create_symlink.asser_has_calls([
            call("/a/functions/hid.usb0", "/a/configs/c.1/hid.usb0")
        ])
