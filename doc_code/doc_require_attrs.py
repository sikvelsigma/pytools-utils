import sys
sys.path.insert(0, 'src/')

# splice@:req_attrs
from pyuseful.classtools.require import RequireAttrs

class Test(RequireAttrs):
    # self.a and self.b must be set by the end of init
    require = ("a", "b")
    def __init__(self):
        self.a = 1
        self.b = 2

t = Test()
# /splice@:req_attrs