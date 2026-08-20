A dictionary lets us associate a key with a value.


"city"
   ↓
hash the key
   ↓
determine location
   ↓
find associated value
   ↓
"Chennai"



<class 'dict_keys'>
<class 'dict_values'>
<class 'dict_items'> - key-value tuples

get()     → safely get a value
keys()    → dict_keys view
values()  → dict_values view
items()   → dict_items view of (key, value) tuples
pop()       → remove + return value
update()    → add/update multiple pairs
setdefault()  → can mutate
- key exists    → return existing value
- key missing   → add default + return default

| Method         | Purpose          | Mutates?    |
| -------------- | ---------------- | ----------- |
| `get()`        | Safely retrieve  | ❌           |
| `keys()`       | Keys view        | ❌           |
| `values()`     | Values view      | ❌           |
| `items()`      | Key-value view   | ❌           |
| `pop()`        | Remove + return  | ✅           |
| `update()`     | Add/update pairs | ✅           |
| `setdefault()` | Get/add default  | Sometimes ✅ |
