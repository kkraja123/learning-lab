## L12 — Control Flow / Conditions

### 1. `if / elif / else`

```python
if condition:
    ...
elif condition:
    ...
else:
    ...
```

* Only the **first matching branch** runs.
* Separate `if` statements are evaluated independently.

### 2. Truthiness

Falsy values include:

```text
False, None, 0, "", [], {}, (), set()
```

Non-empty containers and most other values are truthy.

```python
if value:
```

checks **truthiness**, not whether a variable is bound.

### 3. Logical operators

```text
and → both conditions must be truthy
or  → at least one must be truthy
not → opposite truth value
```

### 4. Short-circuiting

```text
False and ... → stops
True  or  ... → stops
```

The remaining expression may never be evaluated.

### 5. `and` / `or` return operands

```python
10 and 20   # 20
0 and 20    # 0

10 or 20    # 10
0 or 20     # 20
```

### 6. Operator precedence

```text
and → higher precedence
or  → lower precedence
```

So:

```python
A or B and C
```

means:

```python
A or (B and C)
```

### 7. Comparisons

```text
==  → equal value
!=  → not equal
>   → greater
<   → smaller
>=  → greater/equal
<=  → smaller/equal
```

### 8. `==` vs `is`

```text
== → same value
is → same object
```

### 9. Membership

```python
x in collection
x not in collection
```

Checks whether a value exists.

### 10. Conditional expression

```python
result = "Adult" if age >= 18 else "Minor"
```

### Core mental model

> **`if` makes decisions, truthiness determines conditions, and `and`/`or` control how conditions are combined and evaluated.**

**L12 complete. ✅**
