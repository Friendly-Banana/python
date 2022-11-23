import time

def time_it(func, *args, tries=10, name="func", precision=0.8):
    dur = []
    for i in range(tries):        
        start = time.process_time() # perf_counter
        func(*args)
        end = time.process_time() # process_time
        dur.append(end - start)
        #print(f"{name} took {end - start:{precision}f}")
    print(name)
    print(f"tries: {tries}")
    #print(f"times: {dur}") 
    print(f"average: {sum(dur)/tries:{precision}f}")
    print(f"total: {sum(dur):{precision}f}\n")

def compare(*functions:dict):
    for func in functions.keys:
        time_it(func, dict[func])
   
import os
time_it(os.system, "adb --help", name="test", tries=1)