from classtools.immutable import ImmutableProperties
from classtools.postinit import PostInit
from decorators.require import require_condition
from decorators.timing import timing

from classtools.require import RequireAttrs

class Test(ImmutableProperties, PostInit):
    def __init__(self):
        print("init")

    def __postinit__(self):
        print("postinit test")



class Test2(Test):
    require_a_cond = require_condition(cond="self.__a==self._b")
    def __init__(self):
        super().__init__()
        self.__a = 100
        self._b = 100

    def __postinit__(self):
        print("postinit test2")
        super().__postinit__()

    @require_a_cond
    @timing(printout=True)
    def test(self):
        print("summing")
        sum = 0
        for i in range(100000):
            sum += i

class Test3(RequireAttrs):
    require = ("a", "b")


    def __init__(self) -> None:
        self.a=1
        self.b=2


if __name__ == "__main__":
    t = Test3()
