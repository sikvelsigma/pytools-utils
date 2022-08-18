import sys
sys.path.insert(0, '../')

from src.pyuseful.classtools.immutable import ImmutableProperties
from src.pyuseful.classtools.message import MessageThread
from src.pyuseful.classtools.require import RequireAttrs, RequireDictParser
from src.pyuseful.classtools.postinit import PostInit
from src.pyuseful.decorators.require import require_condition, once, limit
from src.pyuseful.decorators.timing import time_exec
from src.pyuseful.decorators.thread import repeat_timer

import time

@repeat_timer(1, get_nones=False, get_false=False)
def fun(msg):
    print(msg)
    return len(msg)


a = fun("hi")
b = fun("hello")

time.sleep(2)

print(a.get())
print(b.get())

time.sleep(2)

print(a.get())

a.stop()
print(a._thread.is_alive())
print(b._thread.is_alive())
print("done")