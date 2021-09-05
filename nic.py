import subprocess
import re

cmd = "wmic nic get AdapterType, Name, Installed, MACAddress, GUID, Manufacturer, Availability, NetConnectionID, PowerManagementSupported, Speed."
#cmd = "ipconfig"
p1 = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
out, err = p1.communicate()

print('out: {0}'.format(out))
print('error : {0}'.format(err))

if p1.returncode == 0:
    print('command : success')
else:
    print('command : failed')


with open('text.txt', 'r') as file:
    filedata = file.read()

ver=re.sub("VERSION:1.1","VERSION:1.2",filedata)

with open('text.txt', 'w') as file:
    file.write(ver)
