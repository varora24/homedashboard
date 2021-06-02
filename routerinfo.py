import pprint
import datetime
from pynetgear import Netgear

netgear = Netgear(password="*******")
devices = netgear.get_attached_devices()

routerinfo = netgear.get_info()

list = []
list.append(routerinfo)
list.append(devices)
