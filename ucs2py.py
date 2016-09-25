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
ucsm_ip = "192.168.222.128"
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
#ucsguilaunch.ucs_gui_launch(handle)

from ucsmsdk.utils import converttopython
converttopython.convert_to_ucs_python()

handle.commit()

# Create a VLAN 11, name prefix = py-
##### Start-Of-PythonScript #####

from ucsmsdk.mometa.fabric.FabricVlan import FabricVlan

mo = FabricVlan(parent_mo_or_dn="fabric/lan", sharing="none", name="py-", id="11", mcast_policy_name="", policy_owner="local", default_net="no", pub_nw_name="", compression_type="included")
handle.add_mo(mo)

handle.commit()
##### End-Of-PythonScript #####


# Create a organization name PY under root
##### Start-Of-PythonScript #####

from ucsmsdk.mometa.org.OrgOrg import OrgOrg

mo = OrgOrg(parent_mo_or_dn="org-root", name="PY", descr="Python test script")
handle.add_mo(mo)

handle.commit()
##### End-Of-PythonScript #####



# Create local boot policy in PY organization
##### Start-Of-PythonScript #####

from ucsmsdk.mometa.lsboot.LsbootPolicy import LsbootPolicy
from ucsmsdk.mometa.lsboot.LsbootVirtualMedia import LsbootVirtualMedia
from ucsmsdk.mometa.lsboot.LsbootStorage import LsbootStorage
from ucsmsdk.mometa.lsboot.LsbootLocalStorage import LsbootLocalStorage
from ucsmsdk.mometa.lsboot.LsbootDefaultLocalImage import LsbootDefaultLocalImage

mo = LsbootPolicy(parent_mo_or_dn="org-root/org-PY", name="PY_LOCAL", descr="boot from local first", reboot_on_update="no", policy_owner="local", enforce_vnic_name="yes", boot_mode="legacy")
mo_1 = LsbootVirtualMedia(parent_mo_or_dn=mo, access="read-only", lun_id="0", mapping_name="", order="1")
mo_2 = LsbootStorage(parent_mo_or_dn=mo, order="2")
mo_2_1 = LsbootLocalStorage(parent_mo_or_dn=mo_2, )
mo_2_1_1 = LsbootDefaultLocalImage(parent_mo_or_dn=mo_2_1, order="2")
handle.add_mo(mo)

handle.commit()
##### End-Of-PythonScript #####


# Create RAID 1 policy in PY organization

##### Start-Of-PythonScript #####

from ucsmsdk.mometa.storage.StorageLocalDiskConfigPolicy import StorageLocalDiskConfigPolicy

mo = StorageLocalDiskConfigPolicy(parent_mo_or_dn="org-root/org-PY", protect_config="yes", name="PY_RAID1", descr="", flex_flash_raid_reporting_state="disable", flex_flash_state="disable", policy_owner="local", mode="raid-mirrored")
handle.add_mo(mo)

handle.commit()
##### End-Of-PythonScript #####

# Create RAID 1 policy in ROOT organization
##### Start-Of-PythonScript #####

from ucsmsdk.mometa.storage.StorageLocalDiskConfigPolicy import StorageLocalDiskConfigPolicy

mo = StorageLocalDiskConfigPolicy(parent_mo_or_dn="org-root", protect_config="yes", name="ROOT_RAID1", descr="", flex_flash_raid_reporting_state="disable", flex_flash_state="disable", policy_owner="local", mode="raid-mirrored")
handle.add_mo(mo)

handle.commit()
##### End-Of-PythonScript #####


# Create UUID Pool in PY organization
##### Start-Of-PythonScript #####

from ucsmsdk.mometa.uuidpool.UuidpoolPool import UuidpoolPool
from ucsmsdk.mometa.uuidpool.UuidpoolBlock import UuidpoolBlock

mo = UuidpoolPool(parent_mo_or_dn="org-root/org-PY", policy_owner="local", prefix="derived", descr="", assignment_order="sequential", name="PY_UUID")
mo_1 = UuidpoolBlock(parent_mo_or_dn=mo, to="2000-000000000040", r_from="2000-000000000001")
handle.add_mo(mo)

handle.commit()
##### End-Of-PythonScript #####


# Create Sever pool in PY organization
##### Start-Of-PythonScript #####

from ucsmsdk.mometa.compute.ComputePool import ComputePool
from ucsmsdk.mometa.compute.ComputePooledSlot import ComputePooledSlot
from ucsmsdk.mometa.compute.ComputePooledEnclosureComputeSlot import ComputePooledEnclosureComputeSlot

mo = ComputePool(parent_mo_or_dn="org-root/org-PY", policy_owner="local", name="PY_SERVERS", descr="")
mo_1 = ComputePooledSlot(parent_mo_or_dn=mo, slot_id="1", chassis_id="1")
mo_2 = ComputePooledSlot(parent_mo_or_dn=mo, slot_id="2", chassis_id="1")
mo_3 = ComputePooledEnclosureComputeSlot(parent_mo_or_dn=mo, slot_id="7", server_instance_id="1", chassis_id="2")
mo_4 = ComputePooledEnclosureComputeSlot(parent_mo_or_dn=mo, slot_id="8", server_instance_id="1", chassis_id="2")
handle.add_mo(mo)

handle.commit()
##### End-Of-PythonScript #####

# Create MAC Pool in PY
##### Start-Of-PythonScript #####

from ucsmsdk.mometa.macpool.MacpoolPool import MacpoolPool
from ucsmsdk.mometa.macpool.MacpoolBlock import MacpoolBlock

mo = MacpoolPool(parent_mo_or_dn="org-root/org-PY", policy_owner="local", descr="", assignment_order="sequential", name="PY_MAC")
mo_1 = MacpoolBlock(parent_mo_or_dn=mo, to="00:25:B5:00:00:7F", r_from="00:25:B5:00:00:00")
handle.add_mo(mo)

handle.commit()
##### End-Of-PythonScript #####

# Create KVM IP Pool
##### Start-Of-PythonScript #####

from ucsmsdk.mometa.ippool.IppoolPool import IppoolPool
from ucsmsdk.mometa.ippool.IppoolBlock import IppoolBlock

mo = IppoolPool(parent_mo_or_dn="org-root/org-PY", is_net_bios_enabled="disabled", name="PY_KVM", descr="", policy_owner="local", ext_managed="internal", supports_dhcp="disabled", assignment_order="sequential")
mo_1 = IppoolBlock(parent_mo_or_dn=mo, prim_dns="8.8.8.8", r_from="172.16.185.150", def_gw="172.16.185.1", sec_dns="8.8.4.4", to="172.16.185.165")
handle.add_mo(mo)

handle.commit()
##### End-Of-PythonScript #####



#Enabled CDP in PY organization

##### Start-Of-PythonScript #####

from ucsmsdk.mometa.nwctrl.NwctrlDefinition import NwctrlDefinition
from ucsmsdk.mometa.dpsec.DpsecMac import DpsecMac

mo = NwctrlDefinition(parent_mo_or_dn="org-root", lldp_transmit="disabled", name="PY_Enabled_CDP", lldp_receive="disabled", mac_register_mode="only-native-vlan", policy_owner="local", cdp="enabled", uplink_fail_action="link-down", descr="")
mo_1 = DpsecMac(parent_mo_or_dn=mo, forge="allow", policy_owner="local", name="", descr="")
handle.add_mo(mo)

handle.commit()
##### End-Of-PythonScript #####




# Make port 21,22 server port on Fabric -A 
##### Start-Of-PythonScript #####

from ucsmsdk.mometa.fabric.FabricDceSwSrvEp import FabricDceSwSrvEp

mo = FabricDceSwSrvEp(parent_mo_or_dn="fabric/server/sw-A", name="", auto_negotiate="yes", usr_lbl="", slot_id="1", admin_state="enabled", port_id="21")
handle.add_mo(mo)


from ucsmsdk.mometa.fabric.FabricDceSwSrvEp import FabricDceSwSrvEp

mo = FabricDceSwSrvEp(parent_mo_or_dn="fabric/server/sw-A", name="", auto_negotiate="yes", usr_lbl="", slot_id="1", admin_state="enabled", port_id="22")
handle.add_mo(mo)


handle.commit()
##### End-Of-PythonScript #####


# Make port 23,24 Uplink Port
##### Start-Of-PythonScript #####

from ucsmsdk.mometa.fabric.FabricEthLanEp import FabricEthLanEp

mo = FabricEthLanEp(parent_mo_or_dn="fabric/lan/A", eth_link_profile_name="default", name="", flow_ctrl_policy="default", admin_speed="10gbps", auto_negotiate="yes", usr_lbl="", slot_id="1", admin_state="enabled", port_id="23")
handle.add_mo(mo)


from ucsmsdk.mometa.fabric.FabricEthLanEp import FabricEthLanEp

mo = FabricEthLanEp(parent_mo_or_dn="fabric/lan/A", eth_link_profile_name="default", name="", flow_ctrl_policy="default", admin_speed="10gbps", auto_negotiate="yes", usr_lbl="", slot_id="1", admin_state="enabled", port_id="24")
handle.add_mo(mo)


handle.commit()
##### End-Of-PythonScript #####


# Make port 1,2 of Expansion module Fabric A as server port
##### Start-Of-PythonScript #####

from ucsmsdk.mometa.fabric.FabricDceSwSrvEp import FabricDceSwSrvEp

mo = FabricDceSwSrvEp(parent_mo_or_dn="fabric/server/sw-A", name="", auto_negotiate="yes", usr_lbl="", slot_id="2", admin_state="enabled", port_id="2")
handle.add_mo(mo)


from ucsmsdk.mometa.fabric.FabricDceSwSrvEp import FabricDceSwSrvEp

mo = FabricDceSwSrvEp(parent_mo_or_dn="fabric/server/sw-A", name="", auto_negotiate="yes", usr_lbl="", slot_id="2", admin_state="enabled", port_id="1")
handle.add_mo(mo)


handle.commit()
##### End-Of-PythonScript #####


#Make port 3,4 Expansion module Fabric A as uplink port

##### Start-Of-PythonScript #####

from ucsmsdk.mometa.fabric.FabricEthLanEp import FabricEthLanEp

mo = FabricEthLanEp(parent_mo_or_dn="fabric/lan/A", eth_link_profile_name="default", name="", flow_ctrl_policy="default", admin_speed="10gbps", auto_negotiate="yes", usr_lbl="", slot_id="2", admin_state="enabled", port_id="3")
handle.add_mo(mo)


from ucsmsdk.mometa.fabric.FabricEthLanEp import FabricEthLanEp

mo = FabricEthLanEp(parent_mo_or_dn="fabric/lan/A", eth_link_profile_name="default", name="", flow_ctrl_policy="default", admin_speed="10gbps", auto_negotiate="yes", usr_lbl="", slot_id="2", admin_state="enabled", port_id="4")
handle.add_mo(mo)


handle.commit()
##### End-Of-PythonScript #####


