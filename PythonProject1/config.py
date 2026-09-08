import os
import sys
import platform
import datetime
import time
import socket

os_name = platform.system()
os_version = platform.version()
os_arch = platform.architecture()[0]

now = datetime.datetime.now()
sys_in = sys.path
print(f"{os_name} {os_version} {os_arch} \n  date {now.year}.{now.month}.{now.day} time {now.hour}:{now.minute}:{now.second}:{now.microsecond}")

os_processor = platform.processor()
print(f"{os_processor} \n ")


ipaddress = socket.gethostbyname(socket.gethostname())
print(f"{ipaddress}")

hostname = socket.gethostname()
print(f"{hostname}")

