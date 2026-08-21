# Lesson 3 Summary

## String indexing

- Positive indexing
- Negative indexing
- IndexError

## String slicing

- start:stop
- Half-open interval (stop excluded)
- Positive and negative indices
- Positive and negative steps
- Step as direction + jump size
- Empty slices
- Default values (name[:], name[::2], etc.)

## Memory model

- Variables vs objects
- References
- id()
- Assignment
- Rebinding

## Mutability

- Mutable vs immutable objects
- Why strings behave differently from lists

## Copying

- List slicing creates a new outer list
- String slicing may reuse the same object (CPython optimization)
- Shallow copy
- Nested lists and shared inner objects

## Function preview

- Function parameters are local variables that refer to the passed object.
- Difference between modifying an object and rebinding a local variable.


Yes. **We've completed the core Python data types section.**
Here is the **master cheat sheet** designed for quiz/interview revision. It is compact enough to scan, but covers the important traps.

Sure. We'll replace the individual summaries with **one master cheat sheet** for the Python data types we've covered.

| Data Type              | Ordered | Mutable | Duplicates        | Indexing  | Key / Element Rule                                                     | Membership            | Main Use                    |
| ---------------------- | ------- | ------- | ----------------- | --------- | ---------------------------------------------------------------------- | --------------------- | --------------------------- |
| **List** `[]`          | ✅       | ✅       | ✅                 | ✅         | Any object                                                             | O(n)                  | Ordered collection          |
| **Tuple** `()`         | ✅       | ❌       | ✅                 | ✅         | Elements can be any object; hashable only if all elements are hashable | O(n)                  | Fixed collection            |
| **Set** `{1,2}`        | ❌       | ✅       | ❌                 | ❌         | Elements must be **hashable**                                          | **O(1) avg**          | Unique values / fast lookup |
| **Frozenset**          | ❌       | ❌       | ❌                 | ❌         | Elements must be **hashable**                                          | **O(1) avg**          | Immutable set               |
| **Dictionary** `{k:v}` | ✅*      | ✅       | Keys ❌ / Values ✅ | Key-based | **Keys must be hashable**                                              | **O(1) avg** for keys | Key → value lookup          |
| **String** `""`        | ✅       | ❌       | ✅                 | ✅         | Characters                                                             | O(n)                  | Text                        |
| **Integer** `int`      | —       | ❌       | —                 | —         | Immutable value                                                        | —                     | Whole numbers               |
| **Float** `float`      | —       | ❌       | —                 | —         | Immutable value                                                        | —                     | Decimal numbers             |
| **Boolean** `bool`     | —       | ❌       | —                 | —         | `True` / `False`                                                       | —                     | Conditions                  |
| **None** `None`        | —       | ❌       | —                 | —         | Represents absence of value                                            | —                     | No value                    |

* Dictionaries preserve **insertion order** in modern Python, but dictionary lookup is **key-based**, not index-based.

### ⭐ Quick Decision Cheat Sheet

| Requirement                  | Choose         |
| ---------------------------- | -------------- |
| Need ordered + changeable    | **List**       |
| Need ordered + fixed         | **Tuple**      |
| Need unique values           | **Set**        |
| Need unique + immutable      | **Frozenset**  |
| Need `key → value`           | **Dictionary** |
| Need text                    | **String**     |
| Need whole number            | **Int**        |
| Need decimal                 | **Float**      |
| Need True/False              | **Bool**       |
| Need to represent "no value" | **None**       |

### 🔑 The 5 most important distinctions

```text
List       → ordered + mutable + duplicates
Tuple      → ordered + immutable + duplicates
Set        → unique + mutable + fast membership
Frozenset  → unique + immutable + fast membership
Dict       → key → value + fast key lookup
```

This is the cheat sheet worth keeping for revision.


# 🐍 Python Data Types — Master Cheat Sheet

## 1. Big Picture

Python's commonly used built-in data types:

```text
NUMBERS
├── int
├── float
├── complex

BOOLEAN
└── bool

TEXT
└── str

SEQUENCES
├── list
├── tuple
└── range

MAPPING
└── dict

SETS
├── set
└── frozenset

SPECIAL
└── NoneType → None
```

---

# 2. `int`

Whole numbers.

```python
x = 10
x = -5
x = 0
```

### Properties

```text
Mutable?       ❌
Ordered?       N/A
Indexing?      ❌
Hashable?      ✅
```

Python integers have **arbitrary precision**.

```python
10 ** 100
```

is valid.

### Important

```python
type(10)       # int
10 // 3        # 3
10 / 3         # 3.333...
10 % 3         # 1
2 ** 3         # 8
```

---

# 3. `float`

Decimal numbers.

```python
x = 10.5
```

```text
Mutable?   ❌
Hashable?  ✅
```

### Important trap

Floating-point arithmetic can have precision issues:

```python
0.1 + 0.2
# 0.30000000000000004
```

---

# 4. `complex`

```python
z = 3 + 4j
```

Real + imaginary part.

```python
z.real
z.imag
```

```text
Mutable?   ❌
Hashable?  ✅
```

---

# 5. `bool`

Only:

```python
True
False
```

Important:

```python
type(True)
# bool
```

`bool` is a subclass of `int`:

```python
True == 1    # True
False == 0   # True
```

### Truthy / Falsy

Falsy values include:

```text
False
None
0
0.0
""
[]
()
{}
set()
```

Most other values are truthy.

---

# 6. `str`

Text.

```python
name = "Karthick"
```

### Properties

```text
Ordered?      ✅
Indexing?     ✅
Mutable?      ❌
Hashable?     ✅
```

```python
s = "Python"

s[0]      # 'P'
s[-1]     # 'n'
s[1:4]    # 'yth'
```

### Important

Strings are **immutable**.

```python
s[0] = "J"
```

→ `TypeError`

Methods create/return new strings rather than modifying the original.

```python
s.upper()
s.lower()
s.replace()
s.strip()
```

---

# 7. `list`

Ordered, mutable collection.

```python
numbers = [10, 20, 30]
```

### Properties

```text
Ordered?      ✅
Indexing?     ✅
Mutable?      ✅
Duplicates?   ✅
Hashable?     ❌
```

### Common methods

```python
append(x)     # add one
extend(x)     # add multiple
insert(i, x)  # insert
remove(x)     # remove value
pop(i)        # remove + return
clear()       # remove all
sort()        # mutate
reverse()     # mutate
```

### Important difference

```python
a.append([3, 4])
```

adds **one element**.

```python
a.extend([3, 4])
```

adds **two elements**.

### Membership

```python
x in list
```

→ **O(n)** average.

---

# 8. `tuple`

Ordered, immutable collection.

```python
t = (10, 20, 30)
```

### Properties

```text
Ordered?      ✅
Indexing?     ✅
Mutable?      ❌
Duplicates?   ✅
Hashable?     ✅* 
```

`tuple` is hashable **only if all its elements are hashable**.

```python
(1, 2, 3)       # hashable ✅
(1, [2, 3])     # unhashable ❌
```

### One-element tuple

```python
(10,)    # tuple
(10)     # int
```

The comma creates the tuple.

### Important

```python
t += (40,)
```

doesn't mutate the old tuple.

It creates a **new tuple** and rebinds the name.

---

# 9. `range`

Represents an immutable sequence of numbers.

```python
range(5)
```

Produces:

```text
0 1 2 3 4
```

### Forms

```python
range(stop)

range(start, stop)

range(start, stop, step)
```

### Important

`stop` is **excluded**.

```python
range(1, 5)
# 1, 2, 3, 4
```

### Properties

```text
Ordered?      ✅
Indexing?     ✅
Mutable?      ❌
```

Useful for loops and memory-efficient numeric sequences.

---

# 10. `dict`

Stores **key → value** pairs.

```python
student = {
    "name": "Karthick",
    "age": 28
}
```

### Properties

```text
Mutable?          ✅
Keys unique?      ✅
Values unique?    ❌
Keys hashable?    ✅
Indexing?         ❌
```

### Access

```python
d["name"]
```

Missing key:

```python
d["xyz"]
```

→ `KeyError`

Safe:

```python
d.get("xyz")
```

→ `None`

or:

```python
d.get("xyz", 0)
```

→ `0`

### Important methods

```python
keys()
values()
items()
get()
pop()
update()
setdefault()
clear()
```

### Membership

```python
"x" in d
```

checks **keys**, not values.

```python
10 in d.values()
```

checks values.

### Complexity

Average:

```text
lookup      O(1)
insert      O(1)
update      O(1)
delete      O(1)
membership  O(1)
```

---

# 11. `set`

Collection of **unique hashable values**.

```python
s = {10, 20, 30}
```

### Properties

```text
Unique?       ✅
Mutable?      ✅
Indexing?     ❌
Duplicates?   ❌
Hash-based?   ✅
```

### Membership

```python
30 in s
```

→ **O(1) average**

This is the major DSA advantage.

### Methods

```python
add(x)
update(...)
remove(x)
discard(x)
pop()
clear()
```

### `remove()` vs `discard()`

```text
remove(x)   → missing → KeyError
discard(x)  → missing → nothing
```

### `pop()`

```python
s.pop()
```

Removes and returns an **arbitrary element**.

Don't rely on which one.

---

# 12. Set Operations ⭐

Given:

```python
a = {1, 2, 3}
b = {3, 4, 5}
```

| Operator | Meaning     | Result        |
| -------- | ----------- | ------------- |
| `a & b`  | BOTH        | `{3}`         |
| `a \| b` | ALL         | `{1,2,3,4,5}` |
| `a - b`  | LEFT ONLY   | `{1,2}`       |
| `a ^ b`  | EXACTLY ONE | `{1,2,4,5}`   |

### Memory trick

```text
& → BOTH
| → ALL
- → LEFT ONLY
^ → EXACTLY ONE
```

### Relationships

```python
a.issubset(b)
b.issuperset(a)
a.isdisjoint(b)
```

---

# 13. `frozenset`

Immutable set.

```python
fs = frozenset([1, 2, 3])
```

```text
set        → mutable
frozenset  → immutable
```

Unlike a normal set, a `frozenset` is **hashable**.

Therefore it can be:

```python
d[frozenset([1, 2])] = "value"
```

---

# 14. `None`

Represents **absence of a value**.

```python
x = None
```

Type:

```python
type(None)
# NoneType
```

Important:

```python
x == None     # avoid
x is None     # preferred
```

`None` is a singleton.

---

# 15. Mutable vs Immutable ⭐⭐⭐

This is one of the most important quiz topics.

### Immutable

```text
int
float
complex
bool
str
tuple
range
frozenset
NoneType
```

### Mutable

```text
list
dict
set
```

### Mental model

**Immutable → object cannot be changed.**

**Mutable → object can be changed in-place.**

---

# 16. Hashable vs Unhashable

### Usually hashable

```text
int
float
complex
bool
str
tuple* 
frozenset
```

### Unhashable

```text
list
dict
set
```

`tuple*` means:

> Tuple is hashable only when all contained elements are hashable.

---

# 17. Ordered vs Unordered

### Ordered

```text
str
list
tuple
range
dict
```

### No guaranteed order

```text
set
frozenset
```

⚠️ Don't confuse **ordered** with **mutable**.

For example:

```text
tuple → ordered + immutable
list  → ordered + mutable
```

---

# 18. Indexing

### Supports indexing

```text
str
list
tuple
range
```

```python
x[0]
```

### Does NOT support indexing

```text
set
dict
```

Dictionary uses:

```python
d[key]
```

not:

```python
d[0]
```

unless `0` is actually a key.

---

# 19. Duplicates

### Duplicates allowed

```text
str
list
tuple
```

### Duplicates not allowed

```text
set
dict keys
```

Dictionary **values can duplicate**.

```python
{"a": 10, "b": 10}
```

✅ valid.

---

# 20. The Most Important Comparison

| Type        | Mutable | Ordered |     Index | Duplicates | Hashable |
| ----------- | ------: | ------: | --------: | ---------: | -------: |
| `int`       |       ❌ |       — |         ❌ |          — |        ✅ |
| `float`     |       ❌ |       — |         ❌ |          — |        ✅ |
| `complex`   |       ❌ |       — |         ❌ |          — |        ✅ |
| `bool`      |       ❌ |       — |         ❌ |          — |        ✅ |
| `str`       |       ❌ |       ✅ |         ✅ |          ✅ |        ✅ |
| `list`      |       ✅ |       ✅ |         ✅ |          ✅ |        ❌ |
| `tuple`     |       ❌ |       ✅ |         ✅ |          ✅ |       ✅* |
| `range`     |       ❌ |       ✅ |         ✅ |          — |        ✅ |
| `dict`      |       ✅ |       ✅ | key-based |     keys ❌ |        ❌ |
| `set`       |       ✅ |       ❌ |         ❌ |          ❌ |        ❌ |
| `frozenset` |       ❌ |       ❌ |         ❌ |          ❌ |        ✅ |
| `None`      |       ❌ |       — |         ❌ |          — |        ✅ |

---

# 21. Choosing the Right Type

```text
Need a number?
→ int / float / complex

Need text?
→ str

Need ordered + changeable?
→ list

Need ordered + unchangeable?
→ tuple

Need numeric sequence?
→ range

Need key → value?
→ dict

Need unique values + fast membership?
→ set

Need immutable set?
→ frozenset

Need "no value"?
→ None
```

---

# 22. ⭐ Quiz Traps You MUST Remember

```python
(10)
```

→ `int`

```python
(10,)
```

→ `tuple`

---

```python
{}
```

→ `dict`

```python
set()
```

→ empty `set`

---

```python
"abc"[0]
```

→ `"a"`

```python
[10, 20][0]
```

→ `10`

```python
{10, 20}[0]
```

→ `TypeError`

---

```python
d = {"a": 10}

"a" in d
```

→ `True`

```python
10 in d
```

→ `False`

```python
10 in d.values()
```

→ `True`

---

```python
d["missing"]
```

→ `KeyError`

```python
d.get("missing")
```

→ `None`

---

```python
s.remove(100)
```

→ `KeyError`

```python
s.discard(100)
```

→ no error

---

```python
a = b
```

→ same object/reference

```python
a = b.copy()
```

→ new outer container; nested objects may still be shared

---

```python
a += b
```

⚠️ Don't assume mutation. Behavior depends on the type.

For immutable types like tuple:

```python
t += (4,)
```

→ new object + rebinding.

---

# 🧠 Final 30-Second Revision

```text
LIST
→ ordered + mutable + duplicates + indexing

TUPLE
→ ordered + immutable + duplicates + indexing

SET
→ unique + mutable + no indexing + fast membership

FROZENSET
→ unique + immutable + hashable

DICT
→ key → value + mutable + unique keys + fast key lookup

STRING
→ ordered + immutable + indexing

RANGE
→ immutable numeric sequence

INT/FLOAT/COMPLEX
→ numbers

BOOL
→ True / False

NONE
→ absence of value
```

### The single biggest rule

> **Choose the data type based on what you need the data to do, not just how the data looks.**

This cheat sheet is enough for the **core data-type quizzes we've been practicing**, including the common mutation, reference, hashing, membership, indexing, method, and complexity traps.
