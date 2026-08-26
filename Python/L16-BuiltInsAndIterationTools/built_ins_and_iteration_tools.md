enumerate()
zip()
map()
filter()
sorted()
any()
all()
How these work with iterables and iterators
Quiz/interview traps
Final L16 checkpoint

## enumerate

enumerate(iterable, start)

## zip

zip(x,y)
- stops at shortest iterable

## map

map(function, iterable)

- returns map object

map(double, numbers)          # map object, lazy
[double(x) for x in numbers]  # list, immediately created

- with multiple iterables, stops at shortest iterable


enumerate() → index + value
zip()       → corresponding values from multiple iterables
map()       → passes corresponding values as function arguments
filter()    → function returns True/False   → ORIGINAL values are kept

map    → [FUNCTION(x) for x in ...]
filter → [x for x in ... if FUNCTION(x)]

## filter

- Calls the function for each element too. The function is used as a condition, and only elements for which it returns a truthy value are kept.
- filter() keeps the original elements, not the Boolean results.


any() → At least ONE is truthy
all() → EVERY element is truthy

any → "Can I find at least ONE?"
      Empty → No → False

all → "Can I find ANY violation?"
      Empty → No violation → True

Need index + value?          → enumerate()
Need corresponding values?   → zip()
Need transformation?         → map()
Need selection/filtering?    → filter()
Need ordering?               → sorted()
Need at least one?           → any()
Need all?                    → all()


# 📘 L16 — Iteration Tools & Comprehensions — Full Summary

## 1. `enumerate()` — index + value

Use when you need the **index and element together**.

```python
names = ["Alice", "Bob", "Charlie"]

for index, name in enumerate(names):
    print(index, name)
```

Output:

```text
0 Alice
1 Bob
2 Charlie
```

### Start from a different index

```python
enumerate(names, 1)
```

Output conceptually:

```text
1 Alice
2 Bob
3 Charlie
```

⚠️ `start=1` changes the **index**, not where iteration starts.

---

# 2. `zip()` — pair corresponding elements

```python
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 28]

for name, age in zip(names, ages):
    print(name, age)
```

Conceptually:

```text
("Alice", 25)
("Bob", 30)
("Charlie", 28)
```

### Multiple iterables

```python
zip(names, ages, cities)
```

can produce:

```text
("Alice", 25, "Chennai")
("Bob", 30, "Delhi")
("Charlie", 28, "Mumbai")
```

### Unequal lengths

`zip()` stops at the **shortest iterable**.

```python
zip(
    ["A", "B", "C", "D"],
    [10, 20]
)
```

→

```python
[("A", 10), ("B", 20)]
```

---

# 3. `map()` — transform every element

Syntax:

```python
map(function, iterable)
```

Example:

```python
numbers = [1, 2, 3, 4]

def double(x):
    return x * 2

result = map(double, numbers)
```

Conceptually:

```text
1 → double(1) → 2
2 → double(2) → 4
3 → double(3) → 6
4 → double(4) → 8
```

```python
list(result)
```

→

```python
[2, 4, 6, 8]
```

### Important

`map()` returns a **map object**, which is lazy.

```python
result = map(double, numbers)
```

It doesn't immediately create a list.

---

## `map()` with multiple iterables

```python
def add(a, b):
    return a + b

map(add, [1, 2, 3], [10, 20, 30])
```

Conceptually:

```text
add(1, 10) → 11
add(2, 20) → 22
add(3, 30) → 33
```

→

```python
[11, 22, 33]
```

It stops when the **shortest iterable** is exhausted.

---

# 4. `filter()` — select elements

Syntax:

```python
filter(function, iterable)
```

The function is used as a **condition**.

```python
numbers = [1, 2, 3, 4, 5]

def is_even(x):
    return x % 2 == 0

result = filter(is_even, numbers)
```

Conceptually:

```text
1 → False → skip
2 → True  → keep 2
3 → False → skip
4 → True  → keep 4
5 → False → skip
```

Result:

```python
[2, 4]
```

### 🔑 Critical distinction

`filter()` keeps the **original element**.

It does NOT store the Boolean result.

```text
is_even(2) → True
```

but the result contains:

```text
2
```

not:

```text
True
```

---

# 5. `map()` vs `filter()`

This distinction is extremely important.

### `map()`

```text
TRANSFORM
```

```python
map(double, numbers)
```

→ produces **new/transformed values**.

### `filter()`

```text
SELECT
```

```python
filter(is_even, numbers)
```

→ keeps **original values** that satisfy the condition.

### Mental model 🔒

```text
map()
element → function → NEW VALUE

filter()
element → condition → KEEP/SKIP ORIGINAL
```

---

# 6. Comprehension equivalent

### `map()` style

```python
map(double, numbers)
```

Equivalent:

```python
[double(x) for x in numbers]
```

### `filter()` style

```python
filter(is_even, numbers)
```

Equivalent:

```python
[x for x in numbers if is_even(x)]
```

### Why does the function appear in different places?

Because comprehension syntax is:

```python
[expression for item in iterable if condition]
```

For `map()`:

```python
[double(x) for x in numbers]
 ↑
 transformed value
```

For `filter()`:

```python
[x for x in numbers if is_even(x)]
                         ↑
                      condition
```

### 🔑 Mental model

```text
[ WHAT TO STORE  for  WHERE TO GET IT  if  CONDITION ]
```

---

# 7. `sorted()` — return a sorted copy

```python
numbers = [4, 1, 3, 2]

result = sorted(numbers)
```

Result:

```python
[1, 2, 3, 4]
```

But:

```python
numbers
```

is still:

```python
[4, 1, 3, 2]
```

### `reverse=True`

```python
sorted(numbers, reverse=True)
```

→

```python
[4, 3, 2, 1]
```

### Important distinction

```python
sorted(numbers)
```

→ creates/returns a sorted result.

```python
numbers.sort()
```

→ modifies the original list.

---

# 8. `any()` — at least one truthy

```python
numbers = [0, 0, 3, 0]

any(numbers)
```

→

```python
True
```

Because `3` is truthy.

Mental model:

```text
any() → "Is at least ONE truthy?"
```

---

# 9. `all()` — every element truthy

```python
numbers = [1, 2, 3, 4]

all(numbers)
```

→

```python
True
```

Because every value is truthy.

Mental model:

```text
all() → "Are ALL truthy?"
```

---

## Empty iterable trap ⚠️

```python
any([])
```

→ `False`

```python
all([])
```

→ `True`

Remember:

```text
any([]) → False
all([]) → True
```

---

# 10. Truthiness with `filter()`

You can use `bool` directly:

```python
numbers = [0, 1, 2, "", "hello", None]

list(filter(bool, numbers))
```

Result:

```python
[1, 2, "hello"]
```

Because:

```text
0       → False
1       → True
2       → True
""      → False
"hello" → True
None    → False
```

---

# 11. Comprehension — filter + transform

Example:

```python
numbers = [1, 2, 3, 4, 5]

result = [
    number * 10
    for number in numbers
    if number % 2 == 0
]
```

Execution:

```text
1 → odd  → skip
2 → even → 20
3 → odd  → skip
4 → even → 40
5 → odd  → skip
```

Result:

```python
[20, 40]
```

### Mental model

```text
number
   ↓
condition?
   ↓
True  → transform
False → skip
```

---

# 12. `zip()` + comprehension

Example:

```python
names = ["Alice", "Bob", "Charlie"]
scores = [80, 45, 90]
```

Requirement:

> Keep scores ≥ 50 and multiply them by 2.

```python
result = [
    (name, score * 2)
    for name, score in zip(names, scores)
    if score >= 50
]
```

Result:

```python
[("Alice", 160), ("Charlie", 180)]
```

Breakdown:

```text
zip()
↓
pair name + score

if score >= 50
↓
filter/select

score * 2
↓
transform
```

---

# 13. `zip()` + `filter()` + `map()`

These can also be used as a pipeline.

Example requirement:

> Pair names and scores → keep scores ≥ 50 → add 10 bonus points.

Conceptually:

```text
zip
 ↓
PAIR
 ↓
filter
 ↓
SELECT
 ↓
map
 ↓
TRANSFORM
```

Example:

```python
def is_valid(student):
    name, score = student
    return score >= 50

def add_bonus(student):
    name, score = student
    return (name, score + 10)

result = map(
    add_bonus,
    filter(
        is_valid,
        zip(names, scores)
    )
)

print(list(result))
```

Result:

```python
[("Alice", 90), ("Charlie", 100)]
```

---

# 🧠 L16 Master Cheat Sheet

| Tool          | Purpose                   | Mental model  |
| ------------- | ------------------------- | ------------- |
| `enumerate()` | Index + value             | **INDEX**     |
| `zip()`       | Pair corresponding values | **PAIR**      |
| `map()`       | Transform elements        | **TRANSFORM** |
| `filter()`    | Select elements           | **SELECT**    |
| `sorted()`    | Sort values               | **ORDER**     |
| `any()`       | At least one truthy       | **ONE?**      |
| `all()`       | Every value truthy        | **ALL?**      |

### The most important one:

```text
enumerate → index
zip       → pair
filter    → select
map       → transform
sorted    → order
any       → at least one
all       → everything
```

### Comprehension structure

```python
[expression for item in iterable if condition]
```

Think:

```text
WHAT → WHERE → SHOULD I KEEP IT?
```

---

## ✅ L16 Status

**L16 is complete.** 🎯

You were able to reason through the concepts rather than just memorize syntax, especially:

* iterator state
* lazy objects
* truthiness
* filter vs map
* comprehension execution order
* `zip()` with unequal lengths
* combining `zip()` + filtering + transformation

**Next step:** a short mixed **L16 mastery test**, then we move forward.
