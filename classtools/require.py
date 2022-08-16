from classtools.postinit import PostInit

from abc import abstractclassmethod
from typing import Tuple, Dict, Any, List, Type


class PropertyMissing(Exception):
    """All required properties must be set"""
    pass


class TooManyProperties(Exception):
    """Too many properties in 'require_any'"""
    pass

def _cls_name(obj: Type[object]) -> str:
    return obj.__class__.__name__

class RequireAttrs(PostInit):
    @property
    @abstractclassmethod
    def require(self) -> Tuple[str, ...]:
        """This will require you to set attributes a and b
            require = ('a', 'b')
        """
        pass

    def __postinit__(self) -> None:
        """Check if every required args are set"""
        for arg in self.require:
            if arg not in self.__dict__:
                raise PropertyMissing(f"'{_cls_name(self)}' is missing attribute '{arg}'")
            if self.__dict__[arg] is None:
                raise PropertyMissing(f"'{_cls_name(self)}' attribute '{arg}' must be not None")


# class RequireParser(PostInit):
#     @property
#     @abstractclassmethod
#     def require(self) -> Tuple[str, ...]:
#         """This will require you to set attributes a and b
#             require = ('a', 'b')
#         """
#         pass

#     @property
#     @abstractclassmethod
#     def require_any(self) -> Tuple[Tuple[Tuple[str, ...], int]]:
#         pass

#     def __postinit__(self):
#         """Check if every required args are set"""
#         for arg in self.require:
#             if arg not in self.__dict__:
#                 raise PropertyMissing(f"'{_cls_name(self)}' is missing attribute '{arg}'")
#             if self.__dict__[arg] is None:
#                 raise PropertyMissing(f"'{_cls_name(self)}' attribute '{arg}' must be not None")

#         if self.require_any:
#             for arg in self._get_required_any_keys():
#                 if arg not in self.__dict__:
#                     raise PropertyMissing(f"'{_cls_name(self)}' is missing attribute '{arg}'")
#                 if self.__dict__[arg] is None:
#                     raise PropertyMissing(f"'{_cls_name(self)}' attribute '{arg}' must be not None")

#     def _get_required_any_keys(self):
#         """Returns all property keys in require_any"""
#         if self.require_any:
#             return [y for x in self.require_any for y in x[0]]
#         else:
#             return []