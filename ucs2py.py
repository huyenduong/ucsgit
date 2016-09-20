import os, sys
import getpass
from ucsmsdk.ucshandle import UcsHandle
from ucsmsdk.utils import ucsguilaunch
from ucsmsdk.utils import converttopython

ucsm_ip = "172.16.185.144"
admin = "ucspe"
password = "ucspe"
handle = UcsHandle(ucsm_ip,admin,password)
handle.login()

# using gui login
ucsguilaunch.ucs_gui_launch(handle)

converttopython.convert_to_ucs_python()

