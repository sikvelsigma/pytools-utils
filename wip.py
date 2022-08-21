
def postinit(cls_orig):
    """Adds a call to __postinit__ after init was completed"""
    orig_init = cls_orig.__init__

    def __init__(self, *args, **kwargs):
        
        orig_init(self, *args, **kwargs) 
        self.__postinit__()

    cls_orig.__init__ = __init__ 

    return cls_orig


@postinit
class Test:
    def __init__(self) -> None:
        self.a = 1
        print("hi")
    
    def __postinit__(self):
        print(self.a, "postinit")




t = Test()