from .USBCapability import Capability

DESCRIPTOR = [
    0x05, 0x0c,                     #	Usage Page (Consumer Devices)
    0x09, 0x01,                     #	Usage (Consumer Control)
    0xa1, 0x01,                     #	Collection (Application)
    #0x85, 0x04,                     #	REPORT_ID (4)
    None, None,                     # placeholder for report_id
    0x15, 0x00,                     #	Logical Minimum (0)
    0x25, 0x01,                     #	Logical Maximum (1)
    0x09, 0xe9,                     #	Usage (Volume Up)
    0x09, 0xea,                     #	Usage (Volume Down)
    0x75, 0x01,                     #	Report Size (1)
    0x95, 0x02,                     #	Report Count (2)
    0x81, 0x06,                     #	Input (Data, Variable, Relative)

    0x09, 0xe2,                     #	Usage (Mute)
    0x95, 0x01,                     #	Report Count (1)
    0x81, 0x06,                     #	Input (Data, Variable, Relative)

    0x09, 0xb0,                     #	Usage (Play)
    0x95, 0x01,                     #	Report Count (1)
    0x81, 0x06,                     #	Input (Data, Variable, Relative)

    0x09, 0xb1,                     #	Usage (Pause)
    0x95, 0x01,                     #	Report Count (1)
    0x81, 0x06,                     #	Input (Data, Variable, Relative)

    0x09, 0xb7,                     #	Usage (Stop)
    0x95, 0x01,                     #	Report Count (1)
    0x81, 0x06,                     #	Input (Data, Variable, Relative)

    0x09, 0xb5,                     #	Usage (Next)
    0x95, 0x01,                     #	Report Count (1)
    0x81, 0x06,                     #	Input (Data, Variable, Relative)

    0x09, 0xb6,                     #	Usage (Previous)
    0x95, 0x01,                     #	Report Count (1)
    0x81, 0x06,                     #	Input (Data, Variable, Relative)

    0x09, 0xb3,                     #	Usage (Fast Forward)
    0x95, 0x01,                     #	Report Count (1)
    0x81, 0x06,                     #	Input (Data, Variable, Relative)

    0x09, 0xb4,                     #	Usage (Rewind)
    0x95, 0x01,                     #	Report Count (1)
    0x81, 0x06,                     #	Input (Data, Variable, Relative)

    0x95, 0x06,                     #	Report Count (6) Number of bits remaining in byte
    0x81, 0x07,                     #	Input (Constant, Variable, Relative)
    0xc0                            #	End Collection
]

VOLUME_UP = 0x01
VOLUME_DOWN = 0x02
MUTE = 0x04
PLAY = 0x08
PAUSE = 0x10
STOP = 0x20
NEXT = 0x40
PREVIOUS = 0x80

KEYS = {
    'VOLUME_UP': VOLUME_UP,
    'VOLUME_DOWN': VOLUME_DOWN,
    'MUTE': MUTE,
    'PLAY': PLAY,
    'PAUSE': PAUSE,
    'STOP': STOP,
    'NEXT': NEXT,
    'PREVIOUS': PREVIOUS,
}


class Remote(Capability):
    def press(self, key):
        report = chr(self.report_id) + chr(key) + chr(0)
        self.write_report(report)
        self.write_report(chr(self.report_id) + chr(0) + chr(0))
        return report

    def __getattr__(self, item):
        if item.upper() in KEYS:
            return self.press(KEYS[item.upper()])

        return None

    def get_descriptor(self):
        return DESCRIPTOR

