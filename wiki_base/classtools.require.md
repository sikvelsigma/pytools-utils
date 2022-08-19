# Summery
- <kbd>class `RequireAttrs`</kbd> 

Inhereting from `RequireAttrs` forces you to specify what attributes must be set at the end of `__init__` call by defining `require` tuple
- <kbd>class `RequireDictParser`</kbd>

Inhereting from `RequireDictParser` let's you parse a `dict` (or `json` file) which must containg all attributes specified in `require` tuple and some combination of parameters for each tuple in `require_any` tuple. All remaning attributes not in the `dict` but present in `require_any` msut be set in `set_args` method. `declare_args` must be used for type annotations and inital values (mainly for setting optional args as `None`)


# Contains
## RequireAttrs
```python
# insert@:req_attrs
```

---
## RequireDictParser
```python
# insert@:req_parser

```