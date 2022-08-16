# -----------------------------------------
# ------------Require decorator factory----
# -----------------------------------------
from functools import wraps
from inspect import Attribute
from typing import Callable, Type, Tuple, Dict, Any, Optional

class ConditionUnsatisfied(Exception):
    """Condition is not satisfied"""
    pass

def _mangle_args(self: Type[object], inp: str) -> str:
    """Mangle names starting with 'self.__'

    Args:
        self: subclass of object
        inp: str, contains valuate expression
    """
    return inp.replace("self.__", f"self._{_cls_name(self)}__")

def _mangle_single(self: Type[object], inp: str) -> str:
    """Mangle names starting with '__'
    
    Args:
        self: subclass of object
        inp: str, contains name of an object attribute
    """
    return inp.replace("__", f"_{_cls_name(self)}__") if inp.find("__") == 0 else inp

def _cls_name(obj: Type[object]) -> str:
    return obj.__class__.__name__
# -----------------------------------------
# -----------------------------------------

def require_condition(var: Optional[str] = None, cond: Optional[str] = None, msg: Optional[str] = None) -> Callable:
    """Decorator factory for requiring a condition to be True, if 'cond' is None evaluate 'var' alone
    
    Args:
        var: str, argument name is a class
        cond: str, evaluate condition used by eval(), left side is a value of 'var'
        msg: str, display on error
    """
    if var is None and cond is None:
        raise AttributeError("at least one argument must be provided: 'var', 'cond'")
        
    cond_str = cond if cond is not None else ""
    var_str = f"self.{var}" if var is not None else ""
    msg = msg if msg else f"'{var_str}{cond_str}' must evaluate to 'True'"

    def require_decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(self: Type[object], *args: Tuple[Any], **kwargs: Dict[str, Any]) -> Any:
            nonlocal cond, var
            cond = _mangle_args(self, cond) if cond is not None else None
            var = _mangle_single(self, var) if var is not None else None

            try:
                value = self.__dict__[var] if var is not None else ""
            except KeyError:
                raise AttributeError(f"'{_cls_name(self)}' object has no attribute '{var}'") 

            condition = eval(f"{value}{cond}") if cond is not None else bool(value)
            if not condition:
                raise ConditionUnsatisfied(msg)
                
            return func(self, *args, **kwargs)

        return wrapper

    return require_decorator

# -----------------------------------------
# -----------------------------------------

if __name__ == "__main__":
    pass