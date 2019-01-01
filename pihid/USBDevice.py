from .USBConfig import Config


class Device(object):
    def __init__(self, serialnumber, manufacturer, product_name):
        self.serialnumber = serialnumber
        self.manufacturer = manufacturer
        self.product_name = product_name
        self.vendor_id = "0x1d6b"
        self.product_id = "0x0104"
        self.lang = "0x409"
        self.path = "/sys/kernel/config/usb_gadget/" +product_name.lower().replace(" ", "_")
        self.port_name = "hid.usb0"
        self.protocol = "0"
        self.subclass = "0"
        self.report_length = "8"

        self.configs = []
        cfg = Config()
        cfg.params['MaxPower'] = 250
        self.configs.append(cfg)
        self._functions_counter = 1
        self.functions = {}
        self.function_names = []

    def add(self, name, device):
        device.report_id = self._functions_counter
        device.write_report = write_report
        self.functions[name] = device
        self.function_names.append(name)
        self._functions_counter *= 2

    def __getattr__(self, item):
        if item in self.functions:
            return self.functions[item]
        return None


def write_report(report):
    with open('/dev/hidg0', 'rb+') as fd:
        fd.write(report.encode())
