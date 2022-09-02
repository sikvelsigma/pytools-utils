import sys
sys.path.insert(0, 'src/')

# splice@:req_try
from pyuseful.decorators.require import try_times

# will try calling fun1 2 times, 1st call raises an error
x = -1
@try_times(2)
def fun1(a):
    global x
    x += 1
    b = 1/x
    return b

a = fun1(10)
print(a) # will print '1.0'
# /splice@:req_try

