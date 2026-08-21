| Concept | One-Line Memory |
|---------|------------------|
| Variable | A name that references (points to) an object. |
| Assignment (`=`) | Rebinds a variable to an object; it does **not** copy the object. |
| Mutable | The object's contents can be modified without creating a new object. |
| Immutable | Any modification creates a new object instead of changing the existing one. |
| `==` | Checks whether two objects have the same value. |
| `is` | Checks whether two variables reference the exact same object in memory. |
| `list.copy()` | Creates a new outer list, but nested objects are still shared (shallow copy). |
| `copy.deepcopy()` | Creates a completely independent copy of the object and all nested objects. |
| `None` | A singleton object representing the absence of a value. |
| `is None` | The recommended way to check whether a value is `None`. |
| Mutable default argument | Created only once when the function is defined, not each time it is called. |


# Most Important Lessons

If you remember only these six statements, you'll understand most Python behavior:

- Variables are names, not boxes.
- Objects live in memory; variables only refer to them.
- Assignment changes references, not objects.
- Mutable objects are modified; immutable objects are replaced.
- == compares values, is compares identities.
- Always think in terms of memory, not just syntax.

