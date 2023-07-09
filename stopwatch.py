import time

class Stopwatch:
    def __init__(self): 
        """Stopwatch automatically marks start when initialized."""
        self.start_time = time.time()


    def start(self):
        """Reset the stopwatch."""
        self.start_time = time.time()
    
    def stop(self):
        self.stop_time = time.time()

    def elapsed_seconds(self):
        return self.stop_time - self.start_time

    def stop_and_get_elapsed_seconds(self):
        """Stops the stopwatch and returns the elapsed seconds"""
        self.stop_time = time.time()
        return self.stop_time - self.start_time

    def stop_and_get_elapsed_milliseconds(self):
        """Stops the stopwatch and returns the elapsed milliseconds"""
        self.stop_time = time.time()
        return int((self.stop_time-self.start_time)*1000)
    
 

# w = Stopwatch()
# time.sleep(2.0)
# print(w.stop_and_get_elapsed_milliseconds())

#now = time.gmtime() #same struct with below
now = time.localtime() #can pass seconds here
#print(now[0], now.tm_isdst, now.tm_gmtoff/3600)
print(now)
print(time.strftime("%d %H:%M:%S  Z%z")) #localtime current time is used if nothing is passed

#https://docs.python.org/3/library/time.html
t1 = time.strftime ("%A",time.strptime("11 05 1979","%d %m %Y"))
print(t1)