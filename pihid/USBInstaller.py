import os


class Installer(object):
    def __init__(self, device):
        self.device = device

    def is_installed(self):
        return self._dir_exists(self.device.path)

    def install(self):
        self._create_dirs()
        self._create_files()
        self._create_configs()
        self._create_functions()
        self._enable()

    def _enable(self):
        path = self.device.path
        tmp = os.listdir("/sys/class/udc")
        self._fileputcontent(path + "/UDC",  tmp[0])

    def _create_dirs(self):
        path = self.device.path
        lang = self.device.lang
        if not self._dir_exists(path):
            self._create_dir(path)

        if not self._dir_exists(path + "/strings/" + lang):
            self._create_dir(path + "/strings/" + lang)

        if not self._dir_exists(path + "/configs/c.1/strings/" + lang):
            self._create_dir(path + "/configs/c.1/strings/" + lang)

        if not self._dir_exists(path + "/functions/" + self.device.port_name):
            self._create_dir(path + "/functions/" + self.device.port_name)

    def _create_files(self):
        path = self.device.path
        lang = self.device.lang
        self._fileputcontent(path + "/idVendor", self.device.vendor_id)
        self._fileputcontent(path + "/idProduct", self.device.product_id)
        self._fileputcontent(path + "/bcdDevice", "0x0100")
        self._fileputcontent(path + "/bcdUSB", "0x0200")

        self._fileputcontent(path + "/strings/" + lang + "/serialnumber", self.device.serialnumber)
        self._fileputcontent(path + "/strings/" + lang + "/manufacturer", self.device.manufacturer)
        self._fileputcontent(path + "/strings/" + lang + "/product", self.device.product_name)

    def _create_configs(self):
        path = self.device.path
        lang = self.device.lang
        _id = 0
        for cfg in self.device.configs:
            _id += 1
            self._fileputcontent(path + "/configs/c."+str(_id)+"/strings/" + lang + "/configuration", "Config "+str(_id))
            for k, v in cfg.params.items():
                self._fileputcontent(path + "/configs/c."+str(_id)+"/" + k, str(v))

    def _create_functions(self):
        path = self.device.path
        descriptors = []
        for k in self.device.function_names:
            fun = self.device.functions[k]
            desc = self._get_desc_for_function(fun)
            descriptors += desc
        self._fileputcontent(path + "/functions/" + self.device.port_name + "/report_desc", descriptors, "wb")
        self._fileputcontent(path + "/functions/" + self.device.port_name + "/report_length", self.device.report_length)
        self._fileputcontent(path + "/functions/" + self.device.port_name + "/protocol", "0")
        self._fileputcontent(path + "/functions/" + self.device.port_name + "/subclass", "0")
        self._create_symlink(path + "/functions/" + self.device.port_name, path + "/configs/c.1/" + self.device.port_name)

    def _fileputcontent(self, filename, content, mode="w"):
        with open(filename, mode) as fp:
            if type(content) == str:
                fp.write(content)
            if type(content) == list:
                fp.write(bytearray(content))

    def _create_dir(self, path):
        os.makedirs(path)

    def _dir_exists(self, path):
        return os.path.exists(path)

    def _create_symlink(self, source, target):
        os.symlink(source, target, True)

    def _get_desc_for_function(self, fun):
        desc = fun.get_descriptor().copy()
        idx = desc.index(None)
        desc[idx] = 0x85
        desc[idx+1] = fun.report_id

        return desc