import pprint
import datetime
from pynetgear import Netgear

netgear = Netgear(password="Arora@2003")
devices = netgear.get_attached_devices()

routerinfo = netgear.get_info()

list = []
list.append(routerinfo)
list.append(devices)
