import psutil

psutil.cpu_percent(5)
print('The CPU usage is: ', psutil.cpu_percent(4))

psutil.virtual_memory()
print(psutil.virtual_memory())

psutil.virtual_memory().percent
print(psutil.virtual_memory().percent)

psutil.virtual_memory().available * 100 / psutil.virtual_memory().total
print(psutil.virtual_memory().available * 100 / psutil.virtual_memory().total)