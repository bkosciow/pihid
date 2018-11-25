from .USBConfig import Config


class Device(object):
    def __init__(self, serial_number, manufacturer, product_name):
        self.serial_number = serial_number
        self.manufacturer = manufacturer
        self.product_name = product_name
        self.vendor_id = "0x1d6b"
        self.product_id = "0x0104"
        self.lang = "0x409"
        self.path = "/sys/kernel/config/usb_gadget/" +product_name.lower().replace(" ", "_")

        self.configs = []
        cfg = Config()
        cfg.params['MaxPower'] = 250
        self.configs.append(cfg)

        self.functions = []

    def is_installed(self):
        pass

    def install(self):
        pass
