import sys
from nose.tools import assert_equal
sys.path.append("../../")
from pihid.USBDevice import Device
from pihid.USBInstaller import Installer
from unittest.mock import MagicMock
from unittest.mock import call


class TestUSBInstall(object):
    def setUp(self):
        self.device = Device('serial123', 'main', 'testdevice')
        self.installer = Installer(self.device)

    def test_init(self):
        dev = Device('serial123', 'main', 'testdevice')
        ins = Installer(dev)
        assert_equal(ins.device, dev)

    def test_install_should_call_functions(self):
        self.device.path = "/a"
        self.installer._create_dirs = MagicMock()
        self.installer._create_files = MagicMock()
        self.installer._create_functions = MagicMock()
        self.installer._create_configs = MagicMock()

        self.installer.install()

        self.installer._create_dirs.assert_called_with("/a", "0x409")
        self.installer._create_files.assert_called_with()
        self.installer._create_functions.assert_called_with()
        self.installer._create_configs.assert_called_with()

    def test_dirs_should_be_created(self):
        def always_false(a):
            return False
        self.device.path = "/a"
        self.installer._create_dir = MagicMock()
        self.installer._dir_exists = MagicMock()
        self.installer._dir_exists.side_effect = always_false

        self.installer._create_dirs("/a", "0x101")
        self.installer._create_dir.assert_has_calls([
            call("/a"),
            call("/a/strings/0x101"),
            call("/a/configs/c.1/strings/0x101"),

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
