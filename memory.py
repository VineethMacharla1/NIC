import psutil
# gives a single float value
psutil.cpu_percent(10)
print('The CPU usage is: ', psutil.cpu_percent(4))
# gives an object with many fields
psutil.virtual_memory()
print(psutil.virtual_memory())
# you can convert that object to a dictionary
# dict(psutil.virtual_memory()._asdict())
# print(dict(psutil.virtual_memory()._asdict()))
# you can have the percentage of used RAM
psutil.virtual_memory().percent
print(psutil.virtual_memory().percent)
# you can calculate percentage of available memory
psutil.virtual_memory().available * 100 / psutil.virtual_memory().total
print(psutil.virtual_memory().available * 100 / psutil.virtual_memory().total)