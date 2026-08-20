Sure. **L10 — Dictionaries, short and crisp:**

### What

A dictionary stores **key → value** pairs.

```python
student = {"name": "Karthick", "age": 28}
```

### Why

Fast lookup using a key.

```python
student["age"]   # 28
```

### Core behavior

* **Mutable** → can add/update/delete entries.
* Keys must be **hashable**.
* Values can be duplicated.
* Keys must be unique.
* `d[key]` uses hashing → **O(1) average**.

### Hashing

```text
key → hash → location → value
```

Collisions can happen; Python handles them internally.

### Important key rule

```text
int / str              → ✅
(1, 2)                 → ✅
[1, 2]                 → ❌
([1, 2], 3)            → ❌
```

A tuple is hashable only when its elements are hashable.

### Important methods

```text
get(key, default) → read safely, no mutation
keys()            → keys view
values()          → values view
items()           → (key, value) view
pop(key)          → remove + return value
update(...)       → add/update pairs
setdefault(...)   → get existing OR add default
```

### Key traps

```python
d["missing"]          # KeyError
d.get("missing")      # None
```

```python
"a" in d              # checks keys
10 in d               # does NOT check values
10 in d.values()      # checks values
```

### References

```python
b = a
```

→ same dictionary object.

```python
b = a.copy()
```

→ new outer dictionary, but nested objects can still be shared.

### DSA relevance

**Dictionary = fast key-based lookup.**

Common uses:

* frequency counting
* caching
* mapping IDs → objects
* lookup tables
* two-sum style problems

**L10 is complete. ✅**

**Next: L11 — Sets.**
