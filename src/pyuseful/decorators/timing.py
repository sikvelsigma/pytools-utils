from functools import wraps
from typing import Callable, Tuple, Dict, Any
import time


def time_exec(printout: bool = False) -> Callable:
    """Decorator factory, adds 'last_call_elapsed' and 'total_time' attributes to a fucntion

    Args:
        printout: bool, printout to console
    """
    def timing_base(fun: Callable) -> Callable:
        """decorator for timing"""
        @wraps(fun)
        def wrapper(*args: Tuple[Any], **kwargs: Dict[str, Any]) -> Any:
            start = time.time()
            result = fun(*args, **kwargs)
            end = time.time()
            elapsed = (end-start)*1000.0
            wrapper.last_call_elapsed = elapsed
            try:
                wrapper.total_time = wrapper.total_time + elapsed
            except:
                wrapper.total_time = elapsed
            if printout:
                print(f'{fun.__name__:s} function took {elapsed:.3f} ms')
            return result
        return wrapper
    return timing_base
