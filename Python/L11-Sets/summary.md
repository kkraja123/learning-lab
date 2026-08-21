## L11 — Sets: Short Summary

### What?

Collection of **unique, hashable values**.

```python
s = {1, 2, 3}
```

### Why?

* Remove duplicates
* Fast membership → **O(1) average**
* Set operations
* DSA: track `seen` values

### Key properties

```text
Mutable        ✅
Duplicates     ❌
Indexing       ❌
Ordered        ❌
Hash-based     ✅
```

### Important methods

```text
add(x)       → add one, mutates
update(x)    → add multiple, mutates
remove(x)    → remove; missing → KeyError
discard(x)   → remove; missing → nothing
pop()        → remove arbitrary element
```

### Operations

```text
a & b → BOTH / intersection
a | b → ALL / union
a - b → LEFT ONLY
a ^ b → EXACTLY ONE
```

### Relationships

```text
issubset()    → all elements are inside
issuperset()  → contains all elements
isdisjoint()  → no common elements
```

### Hashability

```text
{1, 2, 3}          ✅
{(1, 2), (3, 4)}   ✅
{[1, 2], [3, 4]}   ❌
```

### Set vs List

```text
List → order + indexing
Set  → uniqueness + fast membership
```

### Immutable version

```text
set        → mutable
frozenset  → immutable + hashable
```

**Core mental model:**

> **Set = "Does this value exist?" — not "What is at index X?"**