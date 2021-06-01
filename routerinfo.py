import pprint
import datetime
from pynetgear import Netgear

netgear = Netgear(password="Arora@2003")
devices = netgear.get_attached_devices()
#for i in devices:
#    pprint.pprint(i[0])

routerinfo = netgear.get_info()
#pprint.pprint(routerinfo)

list = []
list.append(routerinfo)
list.append(devices)
