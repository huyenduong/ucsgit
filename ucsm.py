# -*- coding: utf-8 -*-
# author: huyeduon@cisco.com
import os, sys
import getpass
from ucsmsdk.ucshandle import UcsHandle
from ucsmsdk.utils import ucsguilaunch


ucsm_ip = raw_input('Enter UCS Manager IP Address: ')

# if user enter space, use default ip address
if len(ucsm_ip) == 0:
    ucsm_ip = '10.138.157.117'

admin = raw_input('Enter UCSM Manager Administrator: ')
print 'UCS Manager Password:'
password = getpass.getpass()

# If user enter without input, use default password below:
if len(password) == 0:
    password = 'C1sc0123'

# Create first handle for login
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

from ucsmsdk.utils import converttoucspython
converttoucspython.convert_to_ucs_python()



