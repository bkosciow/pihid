import sys
from nose.tools import assert_equal
from unittest.mock import MagicMock
sys.path.append("../../")
from pihid.USBRemote import Remote
from unittest.mock import call
from pihid.USBRemote import KEYS


class TestUSBDevice(object):
    def setUp(self):
        self.device = Remote()
        self.device.report_id = 4
        self.device.write_report = MagicMock()

    def test_press_volume_up(self):
        assert_equal(self.device.volume_up, chr(4) + chr(1) + chr(0))
        self.device.write_report.assert_has_calls([
            call(chr(4) + chr(1) + chr(0)),
            call(chr(4) + chr(0) + chr(0))
        ])

    def test_press_volume_down(self):
        assert_equal(self.device.volume_down, chr(4) + chr(2) + chr(0))
        self.device.write_report.assert_has_calls([
            call(chr(4) + chr(2) + chr(0)),
            call(chr(4) + chr(0) + chr(0))
        ])

    def test_press_mute(self):
        assert_equal(self.device.mute, chr(4) + chr(4) + chr(0))
        self.device.write_report.assert_has_calls([
            call(chr(4) + chr(4) + chr(0)),
            call(chr(4) + chr(0) + chr(0))
        ])

    def test_press_play(self):
        assert_equal(self.device.play, chr(4) + chr(8) + chr(0))
        self.device.write_report.assert_has_calls([
            call(chr(4) + chr(8) + chr(0)),
            call(chr(4) + chr(0) + chr(0))
        ])

    def test_press_pause(self):
        assert_equal(self.device.pause, chr(4) + chr(16) + chr(0))
        self.device.write_report.assert_has_calls([
            call(chr(4) + chr(16) + chr(0)),
            call(chr(4) + chr(0) + chr(0))
        ])

    def test_press_stop(self):
        assert_equal(self.device.stop, chr(4) + chr(32) + chr(0))
        self.device.write_report.assert_has_calls([
            call(chr(4) + chr(32) + chr(0)),
            call(chr(4) + chr(0) + chr(0))
        ])

    def test_press_next(self):
        assert_equal(self.device.next, chr(4) + chr(64) + chr(0))
        self.device.write_report.assert_has_calls([
            call(chr(4) + chr(64) + chr(0)),
            call(chr(4) + chr(0) + chr(0))
        ])

    def test_press_previous(self):
        assert_equal(self.device.previous, chr(4) + chr(128) + chr(0))
        self.device.write_report.assert_has_calls([
            call(chr(4) + chr(128) + chr(0)),
            call(chr(4) + chr(0) + chr(0))
        ])

