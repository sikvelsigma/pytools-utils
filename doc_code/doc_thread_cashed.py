import sys
sys.path.insert(0, 'src/')

# splice@:cash_timer
from pyuseful.decorators.thread import cash_timer

import time

# Calls current_time() every 1 sec and stores the result
@cash_timer(timer=1, timeout=10)
def current_time():
    return time.time()

a = current_time()
print(a.get())
time.sleep(2)
print(a.get())
a.stop()
# /splice@:cash_timer