import sys
sys.path.append("../")
from pihid import USBDevice, USBInstaller, USBRemote

dev = USBDevice.Device('123', 'hone', 'rpihone')
dev.add('remote', USBRemote.Remote())
# dev.add('remote1', USBRemote.Remote())
# dev.add('remote2', USBRemote.Remote())
# dev.add('remote3', USBRemote.Remote())

installer = USBInstaller.Installer(dev)

# installer._create_functions()
installer.install()


