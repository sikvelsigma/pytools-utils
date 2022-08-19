import sys
sys.path.insert(0, 'src/')

# splice@:req_parser
from pyuseful.classtools.require import RequireDictParser

class Test(RequireDictParser):
    # keys 'a' and 'b' must in a dict or json file
    require = ("a", "b")     

    require_any = (
        # either key 'x' or 'y' must be in a dict or json file
        (("x", "y"), 1),  
        # either combination must be in a dict or json file: 
        # 'q' & 'w', 'q' & 'e', 'w' & 'e'      
        (("q", "w", "e"), 2)    
    )

    # parse str values as numbers ('True' by default)
    infer_numbers = True

    def declare_args(self):
        """ Typing the attributes or setting init values as 'None',
        will raise an error on trying to set a different value
        """
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
# /splice@:req_parser