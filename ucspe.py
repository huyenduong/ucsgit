# -*- coding: utf-8 -*-
# author: huyeduon@cisco.com
import os, sys
import getpass
from ucsmsdk.ucshandle import UcsHandle
from ucsmsdk.utils import ucsguilaunch

# ucsm_ip = raw_input('Enter UCS Manager IP Address: ')
# if user enter space, use default ip address
# if len(ucsm_ip) == 0:
# ucsm_ip = '172.16.185.141/'

# admin = raw_input('Enter UCSM Manager Administrator: ')
# print 'UCS Manager Password:'
# password = getpass.getpass()

# If user enter without input, use default password below:
# if len(password) == 0:
# password = 'ucspe'

# Create first handle for login
ucsm_ip = "172.16.185.141"
admin = "ucspe"
password = "ucspe"
handle = UcsHandle(ucsm_ip,admin,password)
handle.login()

# Create a service profile named sp_demo
#from ucsmsdk.mometa.ls.LsServer import LsServer

#sp = LsServer(parent_mo_or_dn="org-root", name="sp_demo")
#handle.add_mo(sp)
#handle.commit()

# using gui login
from ucsmsdk.utils import ucsguilaunch
ucsguilaunch.ucs_gui_launch(handle)

from ucsmsdk.utils import converttopython
converttopython.convert_to_ucs_python()

# Create vlan 10-20


from ucsmsdk.mometa.fabric.FabricVlan import FabricVlan

mo = FabricVlan(parent_mo_or_dn="fabric/lan", sharing="none", name="vlrange10", id="10", mcast_policy_name="", policy_owner="local", default_net="no", pub_nw_name="", compression_type="included")
handle.add_mo(mo)


from ucsmsdk.mometa.fabric.FabricVlan import FabricVlan

mo = FabricVlan(parent_mo_or_dn="fabric/lan", sharing="none", name="vlrange11", id="11", mcast_policy_name="", policy_owner="local", default_net="no", pub_nw_name="", compression_type="included")
handle.add_mo(mo)


from ucsmsdk.mometa.fabric.FabricVlan import FabricVlan

mo = FabricVlan(parent_mo_or_dn="fabric/lan", sharing="none", name="vlrange20", id="20", mcast_policy_name="", policy_owner="local", default_net="no", pub_nw_name="", compression_type="included")
handle.add_mo(mo)


from ucsmsdk.mometa.fabric.FabricVlan import FabricVlan

mo = FabricVlan(parent_mo_or_dn="fabric/lan", sharing="none", name="vlrange18", id="18", mcast_policy_name="", policy_owner="local", default_net="no", pub_nw_name="", compression_type="included")
handle.add_mo(mo)


from ucsmsdk.mometa.fabric.FabricVlan import FabricVlan

mo = FabricVlan(parent_mo_or_dn="fabric/lan", sharing="none", name="vlrange19", id="19", mcast_policy_name="", policy_owner="local", default_net="no", pub_nw_name="", compression_type="included")
handle.add_mo(mo)


from ucsmsdk.mometa.fabric.FabricVlan import FabricVlan

mo = FabricVlan(parent_mo_or_dn="fabric/lan", sharing="none", name="vlrange16", id="16", mcast_policy_name="", policy_owner="local", default_net="no", pub_nw_name="", compression_type="included")
handle.add_mo(mo)


from ucsmsdk.mometa.fabric.FabricVlan import FabricVlan

mo = FabricVlan(parent_mo_or_dn="fabric/lan", sharing="none", name="vlrange17", id="17", mcast_policy_name="", policy_owner="local", default_net="no", pub_nw_name="", compression_type="included")
handle.add_mo(mo)


from ucsmsdk.mometa.fabric.FabricVlan import FabricVlan

mo = FabricVlan(parent_mo_or_dn="fabric/lan", sharing="none", name="vlrange14", id="14", mcast_policy_name="", policy_owner="local", default_net="no", pub_nw_name="", compression_type="included")
handle.add_mo(mo)


from ucsmsdk.mometa.fabric.FabricVlan import FabricVlan

mo = FabricVlan(parent_mo_or_dn="fabric/lan", sharing="none", name="vlrange15", id="15", mcast_policy_name="", policy_owner="local", default_net="no", pub_nw_name="", compression_type="included")
handle.add_mo(mo)


from ucsmsdk.mometa.fabric.FabricVlan import FabricVlan

mo = FabricVlan(parent_mo_or_dn="fabric/lan", sharing="none", name="vlrange12", id="12", mcast_policy_name="", policy_owner="local", default_net="no", pub_nw_name="", compression_type="included")
handle.add_mo(mo)


from ucsmsdk.mometa.fabric.FabricVlan import FabricVlan

mo = FabricVlan(parent_mo_or_dn="fabric/lan", sharing="none", name="vlrange13", id="13", mcast_policy_name="", policy_owner="local", default_net="no", pub_nw_name="", compression_type="included")
handle.add_mo(mo)


handle.commit()

# Remove single vlan test-10
mo = handle.query_dn("fabric/lan/net-test-10")
handle.remove_mo(mo)
handle.commit()


# Remove range of vlan 10-15

mo = handle.query_dn("fabric/lan/net-vlrange10")
handle.remove_mo(mo)

mo = handle.query_dn("fabric/lan/net-vlrange11")
handle.remove_mo(mo)

mo = handle.query_dn("fabric/lan/net-vlrange12")
handle.remove_mo(mo)

mo = handle.query_dn("fabric/lan/net-vlrange13")
handle.remove_mo(mo)

mo = handle.query_dn("fabric/lan/net-vlrange14")
handle.remove_mo(mo)

mo = handle.query_dn("fabric/lan/net-vlrange15")
handle.remove_mo(mo)

handle.commit()

# Create vsan 100 on Fabric - A
from ucsmsdk.mometa.fabric.FabricVsan import FabricVsan

mo = FabricVsan(parent_mo_or_dn="fabric/san/A", name="100", fcoe_vlan="1010", policy_owner="local", fc_zone_sharing_mode="coalesce", zoning_state="disabled", id="100")
handle.add_mo(mo)

handle.commit()

# Create vsan 200 on Fabric - B

from ucsmsdk.mometa.fabric.FabricVsan import FabricVsan

mo = FabricVsan(parent_mo_or_dn="fabric/san/B", name="200", fcoe_vlan="1020", policy_owner="local", fc_zone_sharing_mode="coalesce", zoning_state="disabled", id="200")
handle.add_mo(mo)

handle.commit()

