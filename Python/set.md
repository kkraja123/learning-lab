Absolutely. Here is the **complete but crisp L11 — Sets summary**, covering every point we discussed.

# L11 — Sets 📦

### 1. What is a Set?

A **set** is a collection of **unique, hashable elements**.

```python
s = {10, 20, 30}
```

Duplicates are automatically removed:

```python
{10, 20, 10, 30, 20}
# {10, 20, 30}
```

---

### 2. Why use a Set?

Main reasons:

```text
1. Remove duplicates
2. Fast membership checking
3. Set mathematical operations
4. Track "already seen" values in DSA
```

Most important DSA use:

```python
seen = set()

if x in seen:
    # already seen
```

`x in set` → **O(1) average-case**.

---

### 3. Set vs List

| Feature      | List     | Set               |
| ------------ | -------- | ----------------- |
| Ordered      | ✅        | ❌                 |
| Duplicates   | ✅        | ❌                 |
| Indexing     | ✅        | ❌                 |
| Mutable      | ✅        | ✅                 |
| Membership   | O(n)     | O(1) avg          |
| Main purpose | Sequence | Unique membership |

Think:

```text
List → "What is at index 3?"
Set  → "Does this value exist?"
```

---

### 4. Creating Sets

```python
s = {1, 2, 3}
```

Empty set:

```python
s = set()
```

⚠️ This is **not** an empty set:

```python
s = {}
```

That creates an empty **dictionary**.

---

### 5. Duplicates

```python
s = {1, 2, 2, 3, 3}
```

Result:

```python
{1, 2, 3}
```

Sets store each value only once.

---

### 6. Hashing

Sets use **hashing internally**.

Conceptually:

```text
value
  ↓
hash
  ↓
hash table
```

That's why membership is generally:

```text
x in set → O(1) average
```

---

### 7. Set elements must be hashable

Works:

```python
{1, 2, 3}
{"a", "b"}
{(1, 2), (3, 4)}
```

Doesn't work:

```python
{[1, 2], [3, 4]}
```

because lists are **unhashable**.

Important:

> A tuple is hashable only if its elements are hashable.

---

### 8. `add()`

Adds **one element** and mutates the set.

```python
s = {1, 2}

result = s.add(3)
```

```text
s      → {1, 2, 3}
result → None
```

Adding an existing element does nothing:

```python
s.add(2)
```

No duplicate is created.

---

### 9. `update()`

Adds multiple elements and **mutates** the set.

```python
a = {1, 2}
b = {2, 3, 4}

a.update(b)

# a → {1, 2, 3, 4}
```

Compare:

```text
a | b         → new set
a.update(b)   → mutates a
```

---

### 10. `remove()`

Removes an element.

```python
s.remove(20)
```

If the element doesn't exist:

```python
s.remove(50)
```

→ **KeyError**

---

### 11. `discard()`

Removes an element if present.

```python
s.discard(20)
```

If it doesn't exist:

```python
s.discard(50)
```

→ **nothing happens**

Remember:

```text
remove()  → missing → KeyError
discard() → missing → no error
```

---

### 12. `pop()`

Removes and returns an **arbitrary element**.

```python
s = {10, 20, 30}

x = s.pop()
```

`x` could be any of the elements.

Don't rely on which one.

```text
set.pop() → arbitrary element
```

---

### 13. Membership

```python
20 in s
```

→ `True` / `False`

Average:

```text
O(1)
```

This is one of the biggest reasons to use sets.

---

### 14. No indexing

This doesn't work:

```python
s[0]
```

→ `TypeError`

Sets have no positional indexing.

To process elements:

```python
for value in s:
    print(value)
```

Or convert:

```python
list(s)
```

But don't assume the resulting list's order.

---

### 15. Set ordering

Sets are **unordered**.

Don't rely on:

```python
{10, 20, 30}
```

always displaying/iterating in that exact order.

> Unordered does not mean "random"; it means order is not something your code should depend on.

---

# 16. Set Operations

Given:

```python
a = {1, 2, 3}
b = {3, 4, 5}
```

### Intersection `&`

Common elements:

```python
a & b
# {3}
```

**Think: BOTH**

---

### Union `|`

Everything unique from both:

```python
a | b
# {1, 2, 3, 4, 5}
```

**Think: ALL**

---

### Difference `-`

Elements in the **left set only**:

```python
a - b
# {1, 2}
```

**Think: LEFT ONLY**

Direction matters:

```python
b - a
# {4, 5}
```

---

### Symmetric Difference `^`

Elements present in **exactly one** set:

```python
a ^ b
# {1, 2, 4, 5}
```

`3` is excluded because it exists in both.

**Think: EXACTLY ONE**

### Memorize this:

```text
& → BOTH
| → ALL
- → LEFT ONLY
^ → EXACTLY ONE
```

---

### 17. `issubset()`

Checks whether **all elements** of one set exist in another.

```python
a = {1, 2}
b = {1, 2, 3}

a.issubset(b)
# True
```

Think:

> Are **ALL of a's elements** inside b?

---

### 18. `issuperset()`

Checks whether one set contains **all elements** of another.

```python
b.issuperset(a)
# True
```

Relationship:

```text
a = {1, 2}
b = {1, 2, 3}

a ⊂ b
b ⊃ a
```

---

### 19. `isdisjoint()`

Checks whether two sets have **no common elements**.

```python
a = {1, 2}
b = {3, 4}

a.isdisjoint(b)
# True
```

If they share even one element:

```python
a = {1, 2}
b = {2, 3}

a.isdisjoint(b)
# False
```

Think:

```text
No common → True
Any common → False
```

---

### 20. Set Comprehension

Similar to list comprehension:

```python
s = {x * 2 for x in [1, 2, 2, 3]}
```

Result:

```python
{2, 4, 6}
```

Compare:

```text
[x * 2 for x in values]       → list
{x * 2 for x in values}       → set
{x: x * 2 for x in values}    → dictionary
```

---

### 21. Mutation vs new Set

```python
c = a | b
```

Creates a **new set**.

```python
a.update(b)
```

Mutates `a`.

Similarly:

```python
b = a
```

doesn't create a new set.

Both names reference the same object:

```text
a ──┐
    ↓
  SET
    ↑
b ──┘
```

So:

```python
b.add(4)
```

also changes `a`.

---

### 22. `frozenset`

Immutable version of a set:

```python
fs = frozenset([1, 2, 3])
```

You cannot:

```python
fs.add(4)
```

because `frozenset` has no `add()` method → **AttributeError**.

Difference:

```text
set        → mutable
frozenset  → immutable
```

Because `frozenset` is immutable and hashable, it can be used as:

```python
d = {}
d[frozenset([1, 2])] = "value"
```

---

# 23. DSA Decision Rule ⭐

Use a **set** when:

> **You don't care about position/order, but you care whether a value exists or has already appeared.**

Typical problems:

```text
Remove duplicates
Detect duplicates
Track visited values
Fast membership
Find common elements
Find differences
```

### Your core mental model

```text
LIST
→ ordered sequence
→ duplicates allowed
→ index-based access

SET
→ unique values
→ no indexing/order guarantee
→ fast membership
→ hash-based
```

**L11 — Sets: COMPLETE ✅**





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
