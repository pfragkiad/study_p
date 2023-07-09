import time

#number of seconds since Epoch
print(time.time())

#number of ns since Epoch
print(time.time_ns())

#sleep number of seconds
#time.sleep(2.0)

#date string - given seconds since Epoch
print(time.ctime(time.time()+60.0))

print(time.asctime(time.localtime()))

#print(time.ctime(time.time()+60.0))
#print(time.asctime(time.localtime(time.ctime(time.time()+60.0))))

#all below return fractional seconds
print("Performance counter:")
print(time.perf_counter())
time.sleep(2.0)
print(time.perf_counter())

print("Process time:")
print(time.process_time())
time.sleep(2.0)
print(time.process_time())

print("Thread time:")
print(time.thread_time())
time.sleep(2.0)
print(time.thread_time())

import math as m

import sys
print(sys.getsizeof(m.fabs(10)))

x=1