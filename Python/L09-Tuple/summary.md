You're right. Here's the **actual short revision sheet**.

# L9 — Tuples

### What?

Ordered, **immutable** collection.

```python
t = (10, 20, 30)
```

### Why?

Use when data represents a **fixed structure**.

```python
point = (10, 20)
```

### List vs Tuple

| List                  | Tuple                 |
| --------------------- | --------------------- |
| Mutable               | Immutable             |
| Dynamic collection    | Fixed structure       |
| More memory generally | Less memory generally |
| `[1,2]`               | `(1,2)`               |

### Important

**Comma creates tuple:**

```python
(10,)   # tuple
(10)    # int
```

### Packing / Unpacking

```python
t = 10, 20, 30       # packing
a, b, c = t          # unpacking
```

`*` collects remaining values into a **list**:

```python
a, *rest = (1,2,3)
# a=1, rest=[2,3]
```

### Nested Mutable Objects

```python
t = ([1,2], 10)
t[0].append(3)       # ✅
t[0] = [3,4]         # ❌
```

Tuple can't change its elements, but contained mutable objects can change.

### Methods

```python
t.count(x)    # occurrences → O(n)
t.index(x)    # first index → O(n)
```

Missing value with `index()` → `ValueError`.

### Complexity

```text
index access → O(1)
membership   → O(n)
```

### Core Rule

> **Tuple = immutable fixed structure**
> **List = mutable collection**
