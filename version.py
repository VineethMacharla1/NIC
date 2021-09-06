import re

with open('text.txt', 'r') as file:
    filedata = file.read()

ver=re.sub("VERSION:1.1","VERSION:1.2",filedata)

with open('text.txt', 'w') as file:
    file.write(ver)
