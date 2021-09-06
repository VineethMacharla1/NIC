import psutil

psutil.cpu_percent(4)
print('The CPU usage is: ', psutil.cpu_percent(4))

psutil.virtual_memory()
print(psutil.virtual_memory())

psutil.virtual_memory().percent
print(psutil.virtual_memory().percent)

psutil.virtual_memory().available * 100 / psutil.virtual_memory().total
print(psutil.virtual_memory().available * 100 / psutil.virtual_memory().total)

# import psutil
# print(psutil.cpu_percent())
# print(psutil.virtual_memory())  # physical memory usage
# # print('memory % used:', psutil.virtual_memory()[2])
# import psutil
#
# mem = psutil.virtual_memory()
# print(mem)