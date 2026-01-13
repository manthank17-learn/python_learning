import time 
print(time.ctime())

t = time.localtime()
print (t)

t = time.localtime()
print(time.strftime("%Y-%m-%d %H:%M:%S", t))