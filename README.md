# pyusful

The package contains a collection of tool: `classtools`, `decorators`

---

## classtools

Contains `immutable`, `message`, `postinit`, `require`

### <kbd>immutable</kbd>
Contains `ImmutableProperties` class. Inhereting from `ImmutableProperties` allows to set non-private attributes (without '__' prefix) of a class only once
```python
from pyuseful.classtools.immutable import ImmutableProperties

class Test(ImmutableProperties):
    # change all attributes once their value is not None will raise an error
    # except if the attribute has '__' prefix
    def __init__(self):
        self.a = 1
        self.b = 2
        self.__i = 0
    
    def fun(self):
        self.a = 10
    
    def inc(self):
        self.__i += 1

t = Test()
# t.a = 0 # this will raise an error
# t.fun() # this will also raise an error
t.inc() # this will NOT raise an error
```

### <kbd>postinit</kbd>
Contains `PostInit` class, `PostInitMeta` metaclass. Inhereting from `PostInit` adds a call to `__postinit__` method after `__init__` call was completed. Inhereting from `PostInitMeta` is not advised.
```python
from pyuseful.classtools.postinit import PostInit

class Test(PostInit):
    # postinit is called immediately after init
    def __init__(self):
        print("this prints on init")
        self.a = 1

    def __postinit__(self):
        print("this prints after init is done")
        print(self.a)

t = Test()
```

### <kbd>require</kbd>
Contains `RequireAttrs`, `RequireDictParser` classes. Inhereting from `RequireAttrs` forces you to specify what attributes must be set at the end of `__init__` call by defining `require` tuple. Inhereting from `RequireDictParser` let's you parse a `dict` (or `json` file) which must containg all attributes specified in `require` tuple and some combination of parameters for each tuple in `require_any` tuple. All remaning attributes not in the `dict` but present in `require_any` msut be set in `set_args` method. `declare_args` must be used for type annotations and inital values (mainly for setting optional args as `None`)
```python
from pyuseful.classtools.require import RequireAttrs

class Test(RequireAttrs):
    # self.a and self.b must be set by the end of init
    require = ("a", "b")
    def __init__(self):
        self.a = 1
        self.b = 2

t = Test()
```

```python
from pyuseful.classtools.require import RequireDictParser

class Test(RequireDictParser):
    # keys 'a' and 'b' must in a dict or json file
    require = ("a", "b")        
    require_any = (
        # either key 'x' or 'y' must be in a dict or json file
        (("x", "y"), 1),  
        # either combination must be in a dict or json file: 'q' & 'w', 'q' & 'e', 'w' & 'e'      
        (("q", "w", "e"), 2)    
    )

    def declare_args(self):
        # typing the attributes and init values
        self.a: float
        self.b: float

        self.x: float
        self.y: float

        self.q: float = None
        self.w: float = None
        self.e: float = None

    def set_args(self):
        # all remaining unset attributes must be set here
        if self.x:
            self.y = self.x + 1
        else:
            self.x = self.y - 1

        if self.q is None:
            self.q = self.w + self.e
        elif self.w is None:
            self.w = self.q - self.e
        else:
            self.e = self.q - self.w

# to read from json
# t = Test.from_json(<path>)

data = dict(
    a=1.1,
    b=2,
    x="10.1",
    q=100,
    w=200,
)
t = Test(data)

```

### <kbd>message</kbd>
Contains `MessageThread` class. Making an instance of `MessageThread` launches a separate thread which will output messages using `print_func` function provided on init with method `print`. This is useful if there're multiple threads outputing messages which may result in a disjoined output
```python
from pyuseful.classtools.message import MessageThread

def some_print(msg):
    print(f"some_print: {msg}")

msg = MessageThread(print_func=print)

# will print "some_print: hello"
msg.print("hello")
# wait for all messages to print
msg.join()
```
---
## decorators

Contains `require`, `timing`
 
### <kbd>require</kbd>
Contains `require_condition` decorator for use in classes.
```python
from pyuseful.decorators.require import require_condition

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
```

### <kbd>timing</kbd>
Contains `time_exec` decorator. Adds `last_call_elapsed`, `total_time` attributes to a function.
```python
from pyuseful.decorators.timing import time_exec

# 'printout=True' prints 'last_call_elapsed' to console on each call
@time_exec(printout=True)
def func():
    sum = 0
    for i in range(100_000):
        sum += i

func()
```