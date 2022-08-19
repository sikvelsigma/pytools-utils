import sys
sys.path.insert(0, 'src/')

# splice@:req_once
from pyuseful.decorators.require import once

# will always return the 1st called value
@once
def fun1(a):
    return a

# will raise an error on the 2nd call
@once(mode="error")
def fun2(a):
    return a

print(fun1(1))  # will print '1'
print(fun1(2))  # will still print '1'

print(fun2(1)) # will print '1'
# print(fun2(2)) # this will raise an error
# /splice@:req_once

