import time
import os

def time_experiment():
    current_time = time.localtime()
    time_zone = time.timezone
    print(current_time)
    print(time_zone)
    print(time.tzname)
time_experiment()


def os_experiment():
    print(os.name)
os_experiment()