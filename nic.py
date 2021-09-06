import subprocess
import platform
import re

if platform.system() == "Windows":

    cmd = "wmic nic get AdapterType, Name, Installed, MACAddress, GUID, Manufacturer, Availability, NetConnectionID, PowerManagementSupported, Speed."

    B = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
    out, err = B.communicate()
    print('out:Hardware,Device and Ethernet Address {0}'.format(out))

    if B.returncode == 0:
        print('Result : Passed')
    else:
        print("Result : Failed")
        print("err:couldn't find{0}".format(err))

elif platform.system() == "Darwin":

    cmd = "networksetup -listallhardwareports"

    B = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
    out, err = B.communicate()
    print('out:Hardware,Device and Ethernet Address {0}'.format(out))

    if B.returncode == 0:
        print('Result : Passed')
    else:
        print("Result : Failed")
        print("err:couldn't find{0}".format(err))

elif platform.system() == "Linux":

    cmd = "hwinfo"

    B = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
    out, err = B.communicate()
    print('out:Hardware,Device and Ethernet Address {0}'.format(out))

    if B.returncode == 0:
        print('Result : Passed')
    else:
        print("Result : Failed")
        print("err:couldn't find{0}".format(err))



