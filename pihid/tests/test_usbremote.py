import sys
from nose.tools import assert_equal
from unittest.mock import MagicMock
sys.path.append("../../")
from pihid.USBRemote import Remote
from pihid.USBRemote import KEYS


class TestUSBDevice(object):
    def setUp(self):
        self.device = Remote()

    def test_press_volume_up(self):
        self.device.press = MagicMock()
        assert_equal(self.device.volume_up, True)
        self.device.press.assert_called_with(KEYS['VOLUME_UP'])

    def test_press_volume_down(self):
        self.device.press = MagicMock()
        assert_equal(self.device.volume_down, True)
        self.device.press.assert_called_with(KEYS['VOLUME_DOWN'])

    def test_press_mute(self):
        self.device.press = MagicMock()
        assert_equal(self.device.mute, True)
        self.device.press.assert_called_with(KEYS['MUTE'])

    def test_press_play(self):
        self.device.press = MagicMock()
        assert_equal(self.device.play, True)
        self.device.press.assert_called_with(KEYS['PLAY'])

    def test_press_pause(self):
        self.device.press = MagicMock()
        assert_equal(self.device.pause, True)
        self.device.press.assert_called_with(KEYS['PAUSE'])

    def test_press_stop(self):
        self.device.press = MagicMock()
        assert_equal(self.device.stop, True)
        self.device.press.assert_called_with(KEYS['STOP'])

    def test_press_next(self):
        self.device.press = MagicMock()
        assert_equal(self.device.next, True)
        self.device.press.assert_called_with(KEYS['NEXT'])

    def test_press_previous(self):
        self.device.press = MagicMock()
        assert_equal(self.device.previous, True)
        self.device.press.assert_called_with(KEYS['PREVIOUS'])
