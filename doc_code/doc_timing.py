import sys
sys.path.insert(0, 'src/')

# splice@:timing
from pyuseful.decorators.timing import time_exec

# 'printout=True' prints 'last_call_elapsed' to console on each call
@time_exec(printout=True)
def func():
    sum = 0
    for i in range(100_000):
        sum += i

func()
# /splice@:timing