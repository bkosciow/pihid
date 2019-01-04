from .USBCapability import Capability

DESCRIPTOR = [
    0x05, 0x01,  # USAGE_PAGE (Generic Desktop)
    0x09, 0x06,  # USAGE (Keyboard)
    0xa1, 0x01,  # COLLECTION (Application)
    None, None,  #  REPORT_ID ()
    0x05, 0x07,  # USAGE_PAGE (Keyboard)
    0x19, 0xe0,  # USAGE_MINIMUM (Keyboard LeftControl)
    0x29, 0xe7,  # USAGE_MAXIMUM (Keyboard Right GUI)
    0x15, 0x00,  # LOGICAL_MINIMUM (0)
    0x25, 0x01,  # LOGICAL_MAXIMUM (1)
    0x75, 0x01,  # REPORT_SIZE (1)
    0x95, 0x08,  # REPORT_COUNT (8)
    0x81, 0x02,  # INPUT (Data,Var,Abs)
    0x95, 0x01,  # REPORT_COUNT (1)
    0x75, 0x08,  # REPORT_SIZE (8)
    0x81, 0x01,  # INPUT (Cnst,Var,Abs) // 0x03
    0x95, 0x05,
    0x75, 0x01,
    0x05, 0x08,
    0x19, 0x01,
    0x29, 0x05,
    0x91, 0x02,
    0x95, 0x01,
    0x75, 0x03,
    0x91, 0x01,  # 0x03
    0x95, 0x06,  # REPORT_COUNT (6)
    0x75, 0x08,  # REPORT_SIZE (8)
    0x15, 0x00,  # LOGICAL_MINIMUM (0)
    0x25, 0x65,  # LOGICAL_MAXIMUM (101)
    0x05, 0x07,  # USAGE_PAGE (Keyboard)
    0x19, 0x00,  # USAGE_MINIMUM (Reserved (no event indicated))
    0x29, 0x65,  # USAGE_MAXIMUM (Keyboard Application)
    0x81, 0x00,  # INPUT (Data,Ary,Abs)
    0xc0,
]

MOD_NONE = 0
MOD_LCTRL = 0x01
MOD_LSHIFT = 0x02
MOD_LALT = 0x04
MOD_LSUPER = 0x08
MOD_RCTRL = 0x10
MOD_RSHIFT = 0x20
MOD_RALT = 0x40
MOD_RSUPER = 0x80

KEY_a = [MOD_NONE, 0x04]
KEY_A = [MOD_LSHIFT, 0x04]


KEYS = {
    'a': KEY_a,
    'A': KEY_A,
}


class Keyboard(Capability):

    def get_descriptor(self):
        return DESCRIPTOR

    def press(self, key):
        pass
