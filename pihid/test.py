import sys
sys.path.append("../")
from pihid import USBDevice, USBInstaller

dev = USBDevice.Device('123', 'hone', 'rpihone')
installer = USBInstaller.Installer(dev)

installer.install()


