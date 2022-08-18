import sys
sys.path.insert(0, '../')

from src.pyuseful.classtools.immutable import ImmutableProperties
from src.pyuseful.classtools.message import MessageThread
from src.pyuseful.classtools.require import RequireAttrs, RequireDictParser
from src.pyuseful.classtools.postinit import PostInit
from src.pyuseful.decorators.require import require_condition
from src.pyuseful.decorators.timing import time_exec

@time_exec(printout=False)
def fun():
    sum = 0
    for i in range(100_000):
        sum += 1

fun()
fun()
print(fun.total_time)