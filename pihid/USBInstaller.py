import os


class Installer(object):
    def __init__(self, device):
        self.device = device

    def is_installed(self):
        return self._dir_exists(self.device.path)

    def install(self):
        self._create_dirs(self.device.path, self.device.lang)
        self._create_files()
        self._create_configs()
        self._create_functions()

    def _create_dirs(self, path, lang):
        if not self._dir_exists(path):
            self._create_dir(path)

        if not self._dir_exists(path + "/strings/" + lang):
            self._create_dir(path + "/strings/" + lang)

        if not self._dir_exists(path + "/configs/c.1/strings/" + lang):
            self._create_dir(path + "/configs/c.1/strings/" + lang)

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
        id = 0
        for cfg in self.device.configs:
            id += 1
            for k, v in cfg.params.items():
                self._fileputcontent(path + "/configs/c."+str(id)+"/" + k, str(v))

    def _create_functions(self):
        pass

    def _fileputcontent(self, filename, content, mode="w"):
        with open(filename, mode) as fp:
            if type(content) == str:
                fp.write(content)
            if type(content) == list:
                fp.write(bytearray(content))

    def _create_dir(self, path):
        os.makedirs(path)

    def _dir_exists(self, path):
        os.path.exists(path)
