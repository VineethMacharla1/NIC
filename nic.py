import subprocess
import platform

if platform.system() == "Windows":

    cmd = "wmic nic get AdapterType, Name, Installed, MACAddress, GUID, Manufacturer, Availability, NetConnectionID, PowerManagementSupported, Speed."
    #cmd = "ipconfig"
    p2 = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
    out, err = p2.communicate()
    print('out:{0}'.format(out))
    print('error :{0}'.format(err))


elif platform.system() == "Darwin":

    cmd = "networksetup -listallhardwareports"

    D = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
    out, err = D.communicate()
    print('out:{0}'.format(out))
    print('error :{0}'.format(err))


elif platform.system() == "Linux":

    cmd = "hwinfo"

    F = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
    out, err = F.communicate()
    print('out:{0}'.format(out))
    print('error :{0}'.format(err))




