import sys
sys.path.insert(0, '../')

from src.pyuseful.classtools.immutable import ImmutableProperties
from src.pyuseful.classtools.message import MessageThread
from src.pyuseful.classtools.require import RequireAttrs, RequireDictParser
from src.pyuseful.classtools.postinit import PostInit
from src.pyuseful.decorators.require import require_condition
from src.pyuseful.decorators.timing import time_exec


class Test:
    # this style definition checks if the bool() of var is True
    require_ready = require_condition("ready")

    #  this style uses eval() to check condition ('self.a>=self.b' in this example)
    require_big_a = require_condition("a", ">=self.b")

    # you can ommit the first arg and just use `cond`, 'msg' let's you specify error message 
    require_big_b = require_condition(cond="self.b>=self.a", msg="'b' must be equal or bigger than 'a'")


    def __init__(self):
        self.ready = False
        self.a = 0
        self.b = 2
    

    def set_ready(self):
        self.ready = True

    @require_ready
    @require_big_b
    def inc_a(self):
        self.a += 1
    
    @require_ready
    @require_big_a
    def inc_b(self):
        self.b += 1

t = Test()
# t.inc_a()   # bool(ready) == False -> will raise an error 
t.set_ready()    
t.inc_a()     # b>=a == True -> a=1, b=2
# t.inc_b()   # a>=b == False -> will raise an error
t.inc_a()     # b>=a == True -> a=2, b=2
t.inc_b()     # a>=b == True -> a=2, b=3
