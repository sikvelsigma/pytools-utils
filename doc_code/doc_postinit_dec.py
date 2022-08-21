
import sys
sys.path.insert(0, 'src/')

# splice@:postinit_dec
from pyuseful.decorators.postinit import postinit

@postinit
class Test:
    def __init__(self):
        self.a = 1
        print("init")

    def __postinit__(self):
        print(self.a)
        print("postinit")

t = Test()
# /splice@:postinit_dec