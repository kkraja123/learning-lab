# L12 — Control Flow & Conditions — Full Summary

## 1. `if`

Used to execute code **only when a condition is truthy**.

```python
age = 20

if age >= 18:
    print("Adult")
```

Think:

> Evaluate the condition → if truthy → execute the block.

---

# 2. Truthiness

Python doesn't require an `if` condition to literally be `True` or `False`.

```python
if x:
```

Python checks the **truth value** of `x`.

### Common falsy values

```python
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

Example:

```python
x = 10

if x:
    print("Yes")
```

`10` is truthy → `Yes`.

```python
x = 0

if x:
    print("Yes")
else:
    print("No")
```

`0` is falsy → `No`.

### Containers

```text
empty container     → falsy
non-empty container → truthy
```

Examples:

```python
[]       # falsy
[1]      # truthy

""       # falsy
"hello"  # truthy

{}       # falsy
{"a": 1} # truthy
```

---

# 3. `if / elif / else`

Used when you have **multiple possible branches**.

```python
score = 75

if score >= 90:
    print("A")
elif score >= 60:
    print("B")
else:
    print("C")
```

Output:

```text
B
```

### Critical rule

Python executes **only the first matching branch**.

```text
if       → checked
   ↓ false
elif     → checked
   ↓ true
execute
   ↓
STOP
```

It does not continue checking later `elif`s.

---

# 4. Multiple independent `if`s

These are different from `elif`.

```python
score = 75

if score >= 60:
    print("B")

if score >= 70:
    print("Passed")
```

Output:

```text
B
Passed
```

Both conditions are evaluated.

### Remember

```text
if / elif / else
→ one branch

separate if statements
→ each if is independent
```

---

# 5. Nested `if`

An `if` can exist inside another `if`.

```python
if age >= 18:
    if has_id:
        print("Allowed")
```

The inner condition is checked **only if the outer condition is true**.

Equivalent simple form:

```python
if age >= 18 and has_id:
    print("Allowed")
```

Use `and` when the conditions are simply required together.

---

# 6. `and`

`and` requires **both sides to be truthy**.

```text
True  and True  → True
True  and False → False
False and True  → False
False and False → False
```

Mental model:

> **ALL must be true.**

Example:

```python
if age >= 18 and has_id:
    print("Allowed")
```

---

# 7. `or`

`or` requires **at least one side to be truthy**.

```text
True  or True  → True
True  or False → True
False or True  → True
False or False → False
```

Mental model:

> **ANY one can be true.**

Example:

```python
if is_admin or is_owner:
    print("Allowed")
```

---

# 8. `not`

`not` reverses the truth value.

```text
not True  → False
not False → True
```

Example:

```python
is_logged_in = True

if not is_logged_in:
    print("Login required")
else:
    print("Welcome")
```

Output:

```text
Welcome
```

---

# 9. Combining conditions

Example:

```python
age = 25
has_id = True
is_banned = False

if age >= 18 and has_id and not is_banned:
    print("Allowed")
```

Evaluation:

```text
age >= 18 → True
has_id → True
not is_banned → True

True and True and True
→ True
```

---

# 10. Comparison operators

```text
==   equal
!=   not equal
>    greater than
<    less than
>=   greater than or equal
<=   less than or equal
```

Example:

```python
x = 10

x == 10   # True
x != 5    # True
x > 10    # False
x >= 10   # True
```

### Important

```text
=   → assignment
==  → equality comparison
```

```python
x = 10      # assignment
x == 10     # comparison
```

---

# 11. `==` vs `is`

This is extremely important.

### `==`

Checks **value equality**.

```python
a = [1, 2]
b = [1, 2]

a == b
# True
```

They contain the same values.

### `is`

Checks **object identity**.

```python
a is b
# False
```

They are different list objects.

But:

```python
c = a

a is c
# True
```

Because both names refer to the **same object**.

### Mental model

```text
== → "Do they have equal values?"
is → "Are they the exact same object?"
```

---

# 12. Chained comparisons

Python allows:

```python
10 < x < 20
```

Instead of:

```python
x > 10 and x < 20
```

For:

```python
x = 15
```

```text
10 < 15 → True
15 < 20 → True

Result → True
```

---

# 13. `in`

Checks membership.

For strings:

```python
"K" in "Karthick"
# True
```

For lists:

```python
3 in [1, 2, 3]
# True
```

For sets:

```python
3 in {1, 2, 3}
# True
```

For dictionaries:

```python
"a" in {"a": 10}
# True
```

For dictionaries, `in` checks **keys**.

---

# 14. `not in`

Opposite of `in`.

```python
blocked = {"admin", "root"}

"user" not in blocked
# True
```

---

# 15. Conditional expression

Python has a compact one-line `if/else`.

```python
age = 20

result = "Adult" if age >= 18 else "Minor"
```

Read it as:

> `"Adult"` if `age >= 18`, otherwise `"Minor"`.

Result:

```python
"Adult"
```

---

# 16. Short-circuit evaluation

This is one of the most important L12 concepts.

Python sometimes **stops evaluating an expression early** because it already knows the final result.

## `and`

If the left side is falsy:

```python
False and anything
```

Python stops.

Result:

```python
False
```

Example:

```python
x = 0

x != 0 and 10 / x > 5
```

First:

```text
x != 0 → False
```

Therefore Python does **not** evaluate:

```python
10 / x
```

No `ZeroDivisionError`.

---

## `or`

If the left side is truthy:

```python
True or anything
```

Python stops.

Example:

```python
x = 10

x == 10 or 100 / 0 > 5
```

First:

```text
x == 10 → True
```

So Python skips:

```python
100 / 0
```

No error.

### Lock this in

```text
False and ... → STOP
True or ...   → STOP
```

---

# 17. `and` / `or` don't necessarily return `True` or `False`

This is a very Python-specific behavior.

They can return the **actual operand**.

### `or`

```python
10 or 20
# 10
```

Because `10` is truthy.

```python
0 or 20
# 20
```

Because `0` is falsy, so Python continues.

### `and`

```python
10 and 20
# 20
```

Because `10` is truthy, so Python evaluates and returns the second operand.

```python
0 and 20
# 0
```

Because `0` is falsy, Python stops there.

### Mental model

```text
A or B
→ if A is truthy → return A
→ otherwise       → return B
```

```text
A and B
→ if A is falsy  → return A
→ otherwise      → return B
```

---

# 18. Operator precedence: `and` vs `or`

When both are present:

```text
and → higher precedence
or  → lower precedence
```

Therefore:

```python
A or B and C
```

is interpreted as:

```python
A or (B and C)
```

Not:

```python
(A or B) and C
```

### Example

```python
x = 10

x > 5 or x < 0 and 10 / 0
```

Conceptually:

```python
(x > 5) or (x < 0 and 10 / 0)
```

But because:

```text
x > 5 → True
```

the `or` short-circuits.

So `10 / 0` is never reached.

---

# 19. Precedence vs short-circuiting

This was the main area we reinforced.

These are **two different concepts**.

### Precedence

Tells Python **how to group** an expression.

```text
and → higher priority
or  → lower priority
```

### Short-circuiting

Tells Python **when it can stop evaluating**.

```text
False and ... → stop
True or ...   → stop
```

Don't confuse:

> "`and` has higher precedence"

with:

> "`and` is always evaluated first."

Short-circuiting can prevent Python from evaluating part of the expression.

---

# 20. Mixed `and` + `or`

Example:

```python
x = 10
y = 0
z = 20

result = x and y or z
```

Because `and` has higher precedence:

```python
(x and y) or z
```

First:

```text
10 and 0 → 0
```

Then:

```text
0 or 20 → 20
```

Final:

```python
20
```

---

# 21. Common L12 mistakes to avoid

### Mistake 1

Thinking:

```python
if x:
```

means:

> "Does x have an object?"

Instead:

> **"What is the truthiness of the object x refers to?"**

---

### Mistake 2

Thinking `if / elif` checks every condition.

It doesn't.

```text
First True branch → execute → stop
```

---

### Mistake 3

Thinking separate `if`s behave like `elif`.

They don't.

```python
if condition1:
    ...

if condition2:
    ...
```

Both are independently evaluated.

---

### Mistake 4

Confusing `==` and `is`.

```text
== → value equality
is → object identity
```

---

### Mistake 5

Thinking `and`/`or` always return booleans.

They can return actual operands:

```python
10 and 20  # 20
0 or 20    # 20
```

---

### Mistake 6

Seeing an error-producing expression and assuming it will execute.

Example:

```python
False and 10 / 0
```

No error, because the right side is never evaluated.

---

# L12 — Core Mental Model

If you remember only this:

```text
if          → make a decision
truthy      → treated as True
falsy       → treated as False

if/elif     → first matching branch only
separate if → each condition independently

and         → ALL
or          → ANY
not         → opposite

==          → same value
is          → same object

in          → membership
not in      → absence

and         → higher precedence than or

False and X → False, stop
True or X   → True, stop

and/or      → can return actual operands
```

**L12 is complete. ✅**
