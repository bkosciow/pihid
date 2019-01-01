import sys
# sys.path.append("../")
from pihid import USBDevice, USBInstaller, USBRemote

dev = USBDevice.Device('123', 'hone', 'rpihone')
dev.add('remote', USBRemote.Remote())

installer = USBInstaller.Installer(dev)
if not installer.is_installed():
    installer.install()
    exit()

dev.remote.mute
