# L16 — Iteration Tools & Comprehensions 🧠

### 1. `enumerate()`

**Purpose:** Get **index + value**.

```python
for index, value in enumerate(items):
    print(index, value)
```

```text
enumerate(items)     → starts index at 0
enumerate(items, 1)  → starts index at 1
```

**Edge case:** `enumerate()` doesn't skip elements when `start=10`; only the index starts at 10.

---

### 2. `zip()`

**Purpose:** Pair corresponding elements.

```python
zip(names, scores)
```

```text
["A","B"] + [10,20]
→ ("A",10), ("B",20)
```

**Edge case:** Stops at the **shortest iterable**.

```python
list(zip([1,2,3], [10,20]))
# [(1,10), (2,20)]
```

---

### 3. `map()`

**Purpose:** **Transform every element**.

```python
map(function, iterable)
```

```python
list(map(str, [1, 2, 3]))
# ["1", "2", "3"]
```

**Multiple iterables:**

```python
map(add, nums1, nums2)
```

→ `add(1,10)`, `add(2,20)`...

**Edge case:** With multiple iterables, stops at the shortest one.

---

### 4. `filter()`

**Purpose:** **Select elements** based on truthiness.

```python
filter(function, iterable)
```

```python
list(filter(is_even, [1,2,3,4]))
# [2,4]
```

⚠️ `filter()` keeps the **original values**, not `True/False`.

```text
map    → transform → NEW values
filter → select    → ORIGINAL values
```

---

### 5. `sorted()`

**Purpose:** Return a **new sorted list**.

```python
sorted([4,1,3,2])
# [1,2,3,4]
```

```python
sorted(numbers, reverse=True)
# descending
```

⚠️ Does **not modify** original list.

```text
sorted(x) → new list
x.sort()  → modifies x
```

---

### 6. `any()`

**Purpose:** Is **at least one** element truthy?

```python
any([0, 0, 5])
# True
```

### 7. `all()`

**Purpose:** Are **all** elements truthy?

```python
all([1, 2, 3])
# True
```

**Important edge case:**

```python
any([])  # False
all([])  # True
```

---

# Comprehension 🧩

General structure:

```python
[expression for item in iterable if condition]
```

Think:

```text
WHAT → FOR EACH → WHERE/CONDITION
```

Example:

```python
[number * 10 for number in numbers if number % 2 == 0]
```

Execution:

```text
1 → False → skip
2 → True  → 20
3 → False → skip
4 → True  → 40
```

Result:

```python
[20, 40]
```

### `map()` vs comprehension

```python
map(double, numbers)
```

≈

```python
[double(x) for x in numbers]
```

### `filter()` vs comprehension

```python
filter(is_even, numbers)
```

≈

```python
[x for x in numbers if is_even(x)]
```

### Critical distinction

```text
map()
→ function transforms each item

filter()
→ function decides whether original item stays

comprehension
→ expression = what to produce
→ if       = what to keep
```

---

# ⚡ Quick Comparison

| Tool          | Main job               | Returns               |
| ------------- | ---------------------- | --------------------- |
| `enumerate()` | Index + value          | `enumerate` iterator  |
| `zip()`       | Pair values            | `zip` iterator        |
| `map()`       | Transform              | `map` iterator        |
| `filter()`    | Select                 | `filter` iterator     |
| `sorted()`    | Sort                   | **new list**          |
| `any()`       | At least one truthy?   | `bool`                |
| `all()`       | All truthy?            | `bool`                |
| Comprehension | Build/transform/filter | Usually list/set/dict |

### 🔥 Master mental model

```text
Need index?          → enumerate()
Need pairing?        → zip()
Need transformation? → map()
Need selection?      → filter()
Need sorting?        → sorted()
Need ONE truthy?     → any()
Need ALL truthy?     → all()
Need readable inline transformation/filtering?
                     → comprehension
```

**Big edge-case theme:** `enumerate`, `zip`, `map`, and `filter` are **lazy iterator-style objects**; they don't immediately produce a list. `list(...)` materializes their results.
