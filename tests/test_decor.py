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

# @repeat_timer(1, get_nones=False, get_false=False)
# def fun(msg):
#     print(msg)
#     return 1

# a = fun("hi")
# time.sleep(2)
# print(a.get())
# time.sleep(2)
# print(a.get())
# a.stop()

# can be called only 2 times
@limit(2)
def fun():
    print("hi")

fun()  # 1st call is allowed
fun()  # 2nd call is allowed
fun()  # 3rd call, this will raise an error