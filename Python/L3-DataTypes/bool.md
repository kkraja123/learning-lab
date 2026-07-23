# Boolean

- Why True + True == 2
- Why bool behaves like an integer
- Truthiness vs True/False
- Why if []: is False
- Why if "Hello": is True
- How Python decides whether an object is true or false


- True is a boolean object that behaves like the integer value 1 in numeric operations.
- False is a boolean object that behaves like the integer value 0 in numeric operations.

- True and False are boolean objects. The bool class inherits from int, so in numeric operations True behaves like 1 and False behaves like 0.

## Truthiness

"Does this object represent something meaningful?"

If yes → Truthy
If no → Falsy

| Object | `bool(...)` | Reason |
|--------|-------------|--------|
| `0` | `False` | Zero is considered falsy. |
| `10` | `True` | Any non-zero number is truthy. |
| `""` | `False` | Empty string is falsy. |
| `"Python"` | `True` | Non-empty string is truthy. |
| `[]` | `False` | Empty list is falsy. |
| `[1, 2]` | `True` | List contains elements. |
| `{}` | `False` | Empty dictionary is falsy. |
| `{"a": 1}` | `True` | Dictionary contains key-value pairs. |
| `set()` | `False` | Empty set is falsy. |
| `{1, 2}` | `True` | Set contains elements. |


## You've now mastered the important parts of bool:

✅ True and False are boolean objects.
✅ bool is a subclass of int.
✅ True behaves like 1 and False behaves like 0 in numeric operations.
✅ == compares values, not types.
✅ if doesn't require a boolean object; it evaluates an object's truth value.
✅ Empty objects are generally falsy; non-empty objects are generally truthy.