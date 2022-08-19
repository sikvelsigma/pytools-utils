import sys
sys.path.insert(0, 'src/')

# splice@:postint
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
# /splice@:postint