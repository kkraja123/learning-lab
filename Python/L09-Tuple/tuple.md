# L9 — Tuples: Short Summary

### 1. What is a Tuple?

A **tuple is an ordered, immutable collection**.

```python
t = (10, 20, 30)
```

* Ordered → maintains position/index
* Immutable → cannot change its elements
* Allows duplicate values
* Can contain different data types

---

### 2. Why use Tuples?

Use a tuple when the data represents a **fixed structure/group of values**.

```python
point = (10, 20)
student = ("Karthick", 28, "Chennai")
```

Think:

> **Tuple = fixed structure**
> **List = changeable collection**

---

### 3. Tuple Creation — Important Trap

The **comma creates the tuple**, not the parentheses.

```python
a = (10)     # int
b = (10,)    # tuple
c = 10,      # tuple
```

---

### 4. Tuple vs List

|            | Tuple           | List               |
| ---------- | --------------- | ------------------ |
| Mutable    | ❌               | ✅                  |
| Ordered    | ✅               | ✅                  |
| Duplicates | ✅               | ✅                  |
| Indexing   | O(1)            | O(1)               |
| Membership | O(n)            | O(n)               |
| Memory     | Generally less  | Generally more     |
| Use        | Fixed structure | Dynamic collection |

Example:

```python
point = (10, 20)          # fixed pair
students = ["A", "B"]     # collection can grow
```

---

### 5. Immutability ≠ Everything inside is immutable

This is an important interview trap:

```python
data = ([1, 2], 10)

data[0].append(3)     # ✅
```

Why?

The **tuple cannot change its references**, but the list object inside it is mutable.

```text
Tuple
 ├──► List [1, 2]  → can mutate
 └──► 10
```

But:

```python
data[0] = [3, 4]     # ❌
```

tries to replace an element of the tuple.

---

### 6. References & Rebinding

```python
a = (1, 2, 3)
b = a
```

Both reference the **same tuple**:

```python
a is b     # True
```

But:

```python
b += (4,)
```

creates a **new tuple** and rebinds `b`.

```text
a → (1,2,3)

b → (1,2,3,4)
```

Therefore:

```python
a is b     # False
```

---

### 7. Packing & Unpacking

**Packing:**

```python
data = 10, 20, 30
```

→ `(10, 20, 30)`

**Unpacking:**

```python
a, b, c = data
```

→

```text
a = 10
b = 20
c = 30
```

Number of values normally must match number of variables.

Mismatch → `ValueError`.

---

### 8. Extended Unpacking

```python
a, *rest = (10, 20, 30, 40)
```

Result:

```text
a    → 10
rest → [20, 30, 40]
```

`*` collects remaining values into a **list**.

---

### 9. Important Tuple Methods

Tuples mainly have two useful methods:

```python
t.count(value)
```

Counts occurrences.

```python
t.index(value)
```

Returns index of the **first occurrence**.

Both:

```text
Time → O(n)
Space → O(1)
```

If `index()` cannot find the value:

```python
t.index(99)
```

→ `ValueError`

Remember:

```text
Invalid index → IndexError
Value not found → ValueError
```

---

### 10. Tuple Comparison

Tuples compare **left → right**.

```python
(1, 5) < (2, 1)
```

Python sees:

```text
1 < 2
```

and stops.

So:

```python
True
```

This is called **lexicographical comparison**.

---

### 11. Complexity

```text
t[index]       → O(1)
value in t     → O(n)
t.count(x)     → O(n)
t.index(x)     → O(n)
```

---

### 12. DSA Relevance

Very common patterns:

```python
points = [(10, 20), (30, 40)]
edges = [(1, 2), (2, 3)]
intervals = [(1, 5), (8, 12)]
```

Often:

> **List = collection of items**
> **Tuple = fixed representation of one item**

---

### The core mental model

If you remember only this:

> **A tuple is an immutable container whose structure cannot be changed, but objects stored inside it may still be mutable.**

And:

> **Tuple → fixed structure**
> **List → mutable collection**

That's the heart of L9.
