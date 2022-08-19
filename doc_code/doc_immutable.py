import sys
sys.path.insert(0, 'src/')

# splice@:immut
from pyuseful.classtools.immutable import ImmutableProperties

class Test(ImmutableProperties):
    # change all attributes once their value is not None will raise an error
    # except if the attribute starts with str in 'mut_prefix'
    mut_prefix = ("__", )
    def __init__(self):
        self.a = 1
        self.b = 2
        self.__i = 0
    
    def fun(self):
        self.a = 10
    
    def inc(self):
        self.__i += 1

t = Test()
t.inc() # this will NOT raise an error
t.c = 1 # this will NOT raise an error

# t.a = 0 # this will raise an error
# t.fun() # this will also raise an error
# /splice@:immut