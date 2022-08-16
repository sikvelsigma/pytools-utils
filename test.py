
from pyuseful.classtools import ImmutableProperties, PostInit, RequireAttrs, RequireDictParser
from pyuseful.decorators import require_condition, time_exec
from pyuseful.classtools import MessageThread

import time

import json
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
    @time_exec(printout=True)
    def test(self):
        print("summing")
        sum = 0
        for i in range(100000):
            sum += i

class Test3(RequireDictParser, ImmutableProperties):
    require = ("a", "b")
    require_any = (
        (("x", "y", "z"), 2),
    )

    def set_args(self) -> None:
        self.z=123

if __name__ == "__main__":
    td = dict(
        a=1,
        b=2,
        c=3,
        x=4,
        y=5,
        # z=6
    )
    
    t = Test3(td)
    
    # with open("test.json", 'w', encoding='utf-8') as f:
    #     json.dump(td, f, ensure_ascii=False, indent=4)

    print(t.a, t.b, t.c, t.x, t.y, t.z)

    ms = MessageThread(print_func=print)
    time.sleep(1)
    ms.print("test1", "sfsdf", 'sdfsdf', sep=";")
    ms.print("test1")
    ms.print("test1")
    time.sleep(1)
    ms.join()
    ms.print("dfgdg")
    ms.join()