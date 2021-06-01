import pprint
import datetime
from pynetgear import Netgear

netgear = Netgear(password="*******")
devices = netgear.get_attached_devices()
#for i in devices:
#    pprint.pprint(i[0])

routerinfo = netgear.get_info()
#pprint.pprint(routerinfo)

list = []
list.append(routerinfo)
list.append(devices)
