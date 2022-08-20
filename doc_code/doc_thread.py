import sys
sys.path.insert(0, 'src/')

# splice@:thread_timer
from pyuseful.decorators.thread import repeat_timer

import time

@repeat_timer(timer=1, get_nones=False, get_false=False)
def fun(msg):
    print(msg)
    return 1

a = fun("hi")
time.sleep(2)
print(a.get())  # will print [1, 1]
time.sleep(2)
print(a.get())  # will print [1, 1]
a.stop()
# /splice@:thread_timer