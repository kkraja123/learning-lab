## Comprehension

[number * number  for number in numbers]
  ↑                    ↑
expression            iteration

## Filter

What do I want to put in the new list? → first part.
Where do I get values? → for part.
Which values should I keep? → if part.

LIST
[expression for item in iterable if condition]

SET
{expression for item in iterable if condition}

DICTIONARY
{key: value for item in iterable if condition}



# 🐍 L15 — Comprehensions — Full Summary

## 1. What is a comprehension?

A **comprehension** is a compact way to create a new collection from an iterable.

Instead of:

```python
result = []

for x in numbers:
    result.append(x * 2)
```

we can write:

```python
result = [x * 2 for x in numbers]
```

### Mental model

```text
Take each item
     ↓
Optionally filter it
     ↓
Transform it
     ↓
Store the result
```

---

# 2. List Comprehension

Basic syntax:

```python
[expression for item in iterable]
```

Example:

```python
numbers = [1, 2, 3, 4]

result = [x * 2 for x in numbers]
```

Output:

```python
[2, 4, 6, 8]
```

### Parts

```python
[x * 2 for x in numbers]
 ↑              ↑
expression     iteration
```

* `x * 2` → **what to produce**
* `for x in numbers` → **where values come from**
* `[]` → creates a **list**

---

# 3. Transformation

A comprehension can transform every element.

```python
numbers = [1, 2, 3]

result = [x * 10 for x in numbers]
```

Output:

```python
[10, 20, 30]
```

Original list is unchanged:

```text
numbers → [1, 2, 3]
result  → [10, 20, 30]
```

### Important

> A comprehension normally creates a **new collection**. It does not modify the source collection.

---

# 4. Filtering with `if`

Syntax:

```python
[expression for item in iterable if condition]
```

Example:

```python
numbers = [1, 2, 3, 4, 5, 6]

result = [x for x in numbers if x % 2 == 0]
```

Output:

```python
[2, 4, 6]
```

Execution:

```text
1 → odd  → skip
2 → even → keep
3 → odd  → skip
4 → even → keep
5 → odd  → skip
6 → even → keep
```

### Mental model

> **Filter → False = SKIP**

---

# 5. Transformation + Filtering

We can combine both:

```python
result = [x * 2 for x in numbers if x % 2 == 0]
```

For:

```python
numbers = [1, 2, 3, 4]
```

Execution:

```text
1 → odd  → skip
2 → even → 2 × 2 → 4
3 → odd  → skip
4 → even → 4 × 2 → 8
```

Result:

```python
[4, 8]
```

### Execution order

Conceptually:

```text
iterate
   ↓
check condition
   ↓
False → skip
True
   ↓
evaluate expression
   ↓
collect result
```

So:

> **Filter first → transform second → collect**

---

# 6. Conditional Expression in a Comprehension

This is different from filtering.

Example:

```python
result = [x if x > 2 else 0 for x in numbers]
```

For:

```python
numbers = [1, 2, 3, 4]
```

Output:

```python
[0, 0, 3, 4]
```

### Difference

### Filtering

```python
[x for x in numbers if x > 2]
```

```text
1 → skip
2 → skip
3 → keep
4 → keep
```

Result:

```python
[3, 4]
```

### Conditional expression

```python
[x if x > 2 else 0 for x in numbers]
```

```text
1 → use 0
2 → use 0
3 → use 3
4 → use 4
```

Result:

```python
[0, 0, 3, 4]
```

### 🔒 Remember

> **Filtering → False = SKIP**
> **Conditional expression → False = ELSE VALUE**

---

# 7. Truthiness in Comprehensions

The condition doesn't have to be a comparison.

You can write:

```python
[x for x in numbers if x]
```

Python checks the truthiness of `x`.

Example:

```python
items = [0, 1, "", "hello", [], [10]]

result = [x for x in items if x]
```

Output:

```python
[1, "hello", [10]]
```

Because:

```text
0       → falsy
1       → truthy
""      → falsy
"hello" → truthy
[]      → falsy
[10]    → truthy
```

### Important connection

This uses the **truthiness concept** from our earlier Python lessons.

---

# 8. Set Comprehension

A set comprehension uses `{}` with only an expression:

```python
{x * 2 for x in numbers}
```

Example:

```python
numbers = [1, 2, 2, 3, 3, 4]

result = {x * 2 for x in numbers}
```

Output:

```python
{2, 4, 6, 8}
```

Duplicates are removed because **sets contain unique elements**.

### Pattern

```python
{expression for item in iterable}
```

---

# 9. Dictionary Comprehension

Dictionary comprehension uses:

```python
{key: value for item in iterable}
```

Example:

```python
numbers = [1, 2, 3, 4]

result = {x: x * 2 for x in numbers}
```

Output:

```python
{
    1: 2,
    2: 4,
    3: 6,
    4: 8
}
```

### Mental model

Ask:

```text
What is my KEY?
        ↓
What is my VALUE?
        ↓
Where do the items come from?
```

---

# 10. Dictionary Keys Must Be Unique

Example:

```python
numbers = [1, 2, 2, 3]

result = {x: x * 2 for x in numbers}
```

Output:

```python
{1: 2, 2: 4, 3: 6}
```

The duplicate `2` doesn't create another key.

### 🔒 Rule

```text
Dictionary:
Keys   → UNIQUE
Values → CAN repeat
```

---

# 11. Dictionary + Filtering

Example:

```python
numbers = [1, 2, 3, 4, 5, 6]

result = {
    number: number * number
    for number in numbers
    if number % 2 == 0
}
```

Output:

```python
{
    2: 4,
    4: 16,
    6: 36
}
```

Execution:

```text
1 → odd  → skip
2 → even → 2:4
3 → odd  → skip
4 → even → 4:16
5 → odd  → skip
6 → even → 6:36
```

---

# 12. Nested Comprehensions

For nested lists:

```python
matrix = [
    [1, 2],
    [3, 4]
]
```

To flatten:

```python
[x for row in matrix for x in row]
```

Output:

```python
[1, 2, 3, 4]
```

Equivalent normal loop:

```python
result = []

for row in matrix:
    for x in row:
        result.append(x)
```

---

# 13. Preserving Nested Structure

If we want:

```python
[
    [2, 4],
    [6, 8]
]
```

we need:

```python
result = [
    [number * 2 for number in row]
    for row in matrix
]
```

Output:

```python
[
    [2, 4],
    [6, 8]
]
```

### Important distinction

**Flatten:**

```python
[number * 2 for row in matrix for number in row]
```

→

```python
[2, 4, 6, 8]
```

**Preserve structure:**

```python
[[number * 2 for number in row] for row in matrix]
```

→

```python
[[2, 4], [6, 8]]
```

---

# 14. Converting a Normal Loop

Normal loop:

```python
result = []

for number in numbers:
    if number % 2 == 1:
        result.append(number * 10)
```

Comprehension:

```python
result = [
    number * 10
    for number in numbers
    if number % 2 == 1
]
```

Output for `[1, 2, 3, 4, 5]`:

```python
[10, 30, 50]
```

### Conversion technique

Identify:

```text
append(expression)
      ↓
expression

for ...
      ↓
for ...

if ...
      ↓
if ...
```

Then build:

```python
[expression for item in iterable if condition]
```

---

# 15. Three Main Comprehension Forms

### List

```python
[x * 2 for x in numbers]
```

→ `list`

### Set

```python
{x * 2 for x in numbers}
```

→ `set`

### Dictionary

```python
{x: x * 2 for x in numbers}
```

→ `dictionary`

### Quick identification

```text
[]           → list
{x}          → set
{x: y}       → dictionary
```

---

# 16. The Most Important Mental Model

When you see:

```python
[expression for item in iterable if condition]
```

think:

```text
          WHERE?
             ↓
      for item in iterable
             ↓
        SHOULD KEEP?
             ↓
          if condition
             ↓
         WHAT VALUE?
             ↓
          expression
```

Or simply:

> **Iterate → Filter → Transform → Collect**

---

# 🎯 L15 Interview/Quiz Traps We Covered

### Trap 1

```python
[x for x in numbers if x % 2]
```

`x % 2` uses truthiness:

```text
0     → False
nonzero → True
```

Therefore it selects **odd numbers**.

---

### Trap 2

```python
[x if x % 2 == 0 else 0 for x in numbers]
```

This does **not filter**.

It keeps every element and chooses either `x` or `0`.

---

### Trap 3

```python
{x: x * 2 for x in numbers}
```

Dictionary keys are unique.

---

### Trap 4

```python
[x * 2 for x in numbers]
```

Creates a **new list**; it doesn't modify `numbers`.

---

### Trap 5

```python
[x * 2 for x in numbers if x % 2 == 0]
```

The condition is checked **before** the expression is used for the result.

---

# 🏆 L15 Status

**L15 — Comprehensions: CLEARED ✅**

You demonstrated that you can:

* Understand the syntax
* Predict outputs
* Explain execution flow
* Build comprehensions yourself
* Convert loops into comprehensions
* Distinguish filtering from `if/else`
* Use truthiness
* Build list/set/dictionary comprehensions
* Handle nested comprehensions
* Explain dictionary key uniqueness

### 🔒 One-line revision

> **Comprehension = a compact way to iterate over an iterable, optionally filter items, transform them, and create a new collection.**

**Next → L16: Built-ins & Iteration Tools. 🚀**
