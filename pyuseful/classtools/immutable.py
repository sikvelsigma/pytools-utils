# -----------------------------------------
# ------------Immutable properties---------
# -----------------------------------------
from typing import Any, Type
class PropertyImmutable(Exception):
    """Cannot mutate an already set property"""
    pass

def _cls_name(obj: Type[object]) -> str:
    return obj.__class__.__name__
class ImmutableProperties():
    """Immutable properties in class (except with '__')"""

    def __setattr__(self, name: str, value: Any) -> None:
        """After the value is set to not None it cannot be changed"""
        tag = f"{self.__class__.__name__}__"
        if not tag in name:
            try:
                current_value = self.__dict__[name]
            except:
                current_value = None
            if name in self.__dict__ and current_value is not None:
                raise PropertyImmutable(f"Property '{name}' in '{_cls_name(self)}' is immutable")
        self.__dict__[name] = value

if __name__ == "__main__":
    pass