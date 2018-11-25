import sys
sys.path.append("../")
from pihid.USBConfig import Config

c1 = Config()
print(c1.id)
c2 = Config()
print(c2.id)
print(c1.id)