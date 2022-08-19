import sys
sys.path.insert(0, 'src/')

# splice@:req_limit
from pyuseful.decorators.require import limit

@limit(2)
def fun():
    print("hi")

fun()  # 1st call is allowed
fun()  # 2nd call is allowed
# fun()  # 3rd call, this will raise an error
# /splice@:req_limit
