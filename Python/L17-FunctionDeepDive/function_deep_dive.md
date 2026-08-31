# Closures

local     → current function
nonlocal  → nearest enclosing function
global    → module/global scope

- nonlocal tells Python not to create a local variable; instead, modify the variable from the nearest enclosing function scope. ✅

NameError
→ Python tried to find a name at runtime and couldn't.

SyntaxError
→ The code violates Python's syntax/scope rules before execution.

A closure is not simply "a function that is returned."

It's:

A function + its preserved access to variables from an enclosing scope.

The important thing is that the closure preserves the state between calls.

|                | Closure             | Default argument             |
| -------------- | ------------------- | ---------------------------- |
| Example        | `return x`          | `value=x`                    |
| Captures       | Variable binding    | Value at function definition |
| Later `x = 20` | Can see updated `x` | Still has `10`               |

# Decorators

add_messages → decorator function
inner        → wrapper function
greet        → original function, then replaced by inner


*args
→ collects positional arguments

**kwargs
→ collects keyword arguments

*args
→ collect/pack

*args when calling
→ unpack

@add_messages
     ↓
decorator we wrote

@wraps(func)
     ↓
decorator supplied by functools

@wraps(func) preserves important metadata of the original function when we replace it with the wrapper.

Original function
      ↓
@add_messages
      ↓
decorator receives function
      ↓
creates inner()
      ↓
@wraps(func)
      ↓
preserves metadata
      ↓
returns inner
      ↓
name now points to inner

# functools

functools
├── wraps       → preserve function metadata
├── partial     → create a new function with some arguments pre-filled
├── reduce      → repeatedly combine values
└── lru_cache   → cache function results

Absolutely. Here's your **L17 detailed revision summary**, keeping it aligned with exactly what we covered. 🧠

# L17 — Function Deep Dive

## 1. Closures

A **closure** happens when an inner function remembers variables from its enclosing function even after the outer function has finished.

```python
def outer():
    x = 10

    def inner():
        return x

    return inner
```

```python
func = outer()
print(func())
```

Output:

```text
10
```

### Mental model

```text
outer()
 ├── x = 10
 └── inner()
       ↑
       remembers x
```

The important idea:

> **Closure = inner function + remembered enclosing variables**

---

# 2. `nonlocal`

`nonlocal` allows an inner function to **modify a variable from the nearest enclosing function scope**.

```python
def outer():
    x = 10

    def inner():
        nonlocal x
        x = 20

    inner()
    return x
```

Result:

```text
20
```

### Important distinction

```text
local       → current function
nonlocal    → nearest enclosing function
global      → module/global scope
```

`nonlocal` does **not** mean global.

You correctly identified this during the lesson:

> `nonlocal` points to the nearest enclosing function scope.

---

# 3. Decorators

A decorator is a function that **takes another function, modifies/extends its behavior, and returns a function**.

Basic structure:

```python
def decorator(func):

    def inner():
        # additional behavior
        func()

    return inner
```

Then:

```python
@decorator
def greet():
    print("Hello")
```

is equivalent to:

```python
greet = decorator(greet)
```

### Critical mental model

```text
original function
       ↓
   decorator
       ↓
     inner
       ↓
modified behavior
```

---

# 4. What is a Wrapper?

You asked this specifically.

A **wrapper** is simply the function that the decorator creates around the original function.

For example:

```python
def decorator(func):

    def inner():
        func()

    return inner
```

Here:

```text
func  → original function
inner → wrapper
```

`wrapper` is **not special Python syntax**.

It is just a common name programmers give to the inner function.

You can call it:

```python
def inner():
```

or:

```python
def wrapper():
```

or:

```python
def something():
```

The behavior is what matters.

---

# 5. Decorator with `*args` and `**kwargs`

A general-purpose decorator often uses:

```python
def decorator(func):

    def inner(*args, **kwargs):
        return func(*args, **kwargs)

    return inner
```

Why?

Because the original function could have different arguments.

For example:

```python
def add(a, b):
    return a + b
```

The wrapper receives:

```text
args   → positional arguments
kwargs → keyword arguments
```

### Remember

```text
*args
    ↓
collects positional arguments

**kwargs
    ↓
collects keyword arguments
```

---

# 6. Preserving Return Values

This was an important point.

❌ Wrong:

```python
def inner(x):
    func(x) + 1
```

The expression is calculated but **not returned**.

Therefore:

```python
inner(5)
```

returns:

```text
None
```

✅ Correct:

```python
def inner(x):
    return func(x) + 1
```

Now the calculated value is returned.

### Key rule

> **Calculating a value ≠ returning a value.**

---

# 7. `functools.wraps`

When a decorator replaces a function with a wrapper, metadata can be lost.

Example:

```python
def decorator(func):

    def inner():
        return func()

    return inner
```

After decoration, the function name may become:

```python
inner
```

instead of:

```python
greet
```

We solve this using:

```python
from functools import wraps
```

```python
def decorator(func):

    @wraps(func)
    def inner():
        return func()

    return inner
```

### What does `wraps()` preserve?

Important metadata includes:

```text
__name__
__doc__
```

For example:

```python
@decorator
def greet():
    """Say hello."""
```

With `@wraps(func)`:

```python
greet.__name__
```

→

```text
greet
```

and:

```python
greet.__doc__
```

→

```text
Say hello.
```

### Mental model

```text
original function
      ↓
     wraps
      ↓
wrapper keeps important metadata
```

---

# 8. Multiple Decorators

You learned this important rule:

```python
@first
@second
def greet():
    pass
```

is equivalent to:

```python
greet = first(second(greet))
```

### Decoration order

Decorators are applied **bottom → top**:

```text
second
  ↓
first
```

### Execution order

When the function is called:

```text
first
  ↓
second
  ↓
original function
  ↓
second
  ↓
first
```

Example:

```text
First before
Second before
Hello
Second after
First after
```

### Easy rule

```text
@A
@B
def func():
```

means:

```text
Decoration → B → A
Execution  → A → B → func → B → A
```

---

# 9. Decorators Can Modify Return Values

A decorator doesn't only print/log things.

It can change the result.

```python
def add_one(func):

    def inner(x):
        return func(x) + 1

    return inner
```

Original:

```python
def double(x):
    return x * 2
```

After decoration:

```text
double(5)
   ↓
5 × 2
   ↓
10
   ↓
+ 1
   ↓
11
```

So:

```python
double(5)
```

→ `11`

---

# 10. Parameterized Decorators

You learned the more advanced form:

```python
@repeat(3)
def greet():
    ...
```

This is different from:

```python
@decorator
def greet():
    ...
```

### Normal decorator

```python
@decorator
```

roughly means:

```python
func = decorator(func)
```

### Parameterized decorator

```python
@repeat(3)
```

roughly means:

```python
func = repeat(3)(func)
```

There are **three layers**:

```python
def repeat(times):          # Layer 1

    def decorator(func):    # Layer 2

        def inner():        # Layer 3
            ...

        return inner

    return decorator
```

### Why three layers?

Because we have three responsibilities:

```text
repeat()
    ↓
receives configuration: times = 3

decorator()
    ↓
receives the actual function

inner()
    ↓
executes the modified behavior
```

This combines:

* functions returning functions
* closures
* decorators

---

# 11. `functools.partial`

`partial()` creates a **new callable with some arguments pre-filled**.

```python
from functools import partial

def multiply(a, b):
    return a * b

double = partial(multiply, 2)
```

Now:

```python
double(5)
```

is effectively:

```python
multiply(2, 5)
```

Result:

```text
10
```

### Important

`partial()` does **not** execute the function immediately.

```python
double = partial(multiply, 2)
```

means:

```text
create new callable
      ↓
remember a = 2
      ↓
wait for remaining arguments
```

Then:

```python
double(5)
```

actually executes `multiply`.

### Keyword arguments

You can also explicitly specify:

```python
square = partial(power, exponent=2)
```

Then:

```python
square(5)
```

means:

```python
power(5, exponent=2)
```

→ `25`

---

# 12. `functools.reduce`

`reduce()` repeatedly combines elements into **one final value**.

```python
from functools import reduce

numbers = [1, 2, 3, 4]

result = reduce(lambda a, b: a + b, numbers)
```

Trace:

```text
1 + 2 → 3
3 + 3 → 6
6 + 4 → 10
```

Final:

```text
10
```

### Compare with `map()` and `filter()`

```text
map()
 ↓
transform each element
 ↓
many results
```

```text
filter()
 ↓
select elements
 ↓
some original elements
```

```text
reduce()
 ↓
combine repeatedly
 ↓
ONE final result
```

---

# 13. Accumulator

The **accumulator** is the result carried from one reduction step to the next.

For:

```python
[1, 2, 3, 4]
```

with addition:

```text
1 + 2 → 3
       ↑
   accumulator

3 + 3 → 6
       ↑
   accumulator

6 + 4 → 10
        ↑
   final accumulator
```

So:

> **Accumulator = current result carried forward.**

The final accumulator becomes the final result, but the accumulator itself is not defined as "the final result."

---

# 14. `reduce()` Initial Value

You learned that `reduce()` can receive an initial value:

```python
reduce(add, numbers, 10)
```

For:

```python
numbers = [1, 2, 3]
```

the first call becomes:

```python
add(10, 1)
```

Then:

```text
10 + 1 → 11
11 + 2 → 13
13 + 3 → 16
```

Final:

```text
16
```

### Without initial value

```text
add(1, 2)
add(result, 3)
```

### With initial value `10`

```text
add(10, 1)
add(result, 2)
add(result, 3)
```

---

# 15. `functools.lru_cache`

`lru_cache` stores previous function results so repeated calls can avoid recalculation.

```python
from functools import lru_cache

@lru_cache
def square(n):
    print("Calculating...")
    return n * n
```

Then:

```python
square(5)
square(5)
```

The calculation happens only once.

```text
First:
5 → calculate → 25 → cache

Second:
5 → cache → 25
```

So:

```text
Calculating...
25
25
```

---

# 16. Cache Is Based on Arguments

Different arguments create different cache entries.

```python
multiply(2, 3)
multiply(2, 3)
multiply(3, 2)
```

The cache sees:

```text
(2, 3)
(2, 3)  ← same → cached
(3, 2)  ← different → calculate
```

Therefore calculation happens **2 times**.

Even though:

```text
2 × 3 = 6
3 × 2 = 6
```

the argument combinations are different.

---

# 17. `lru_cache` and Hashability

This connected directly back to L3.

```python
@lru_cache
def total(numbers):
    return sum(numbers)
```

Calling:

```python
total([1, 2, 3])
```

raises:

```text
TypeError: unhashable type: 'list'
```

Why?

Because the cache needs to use arguments as keys.

```text
list
 ↓
mutable
 ↓
unhashable
 ↓
❌ cannot be cache key
```

A tuple can work:

```python
total((1, 2, 3))
```

provided all elements inside the tuple are themselves hashable.

### Important precision

Not every tuple is automatically hashable.

```python
(1, 2, 3)       → ✅ hashable
("a", "b")       → ✅ hashable
([1, 2], 3)      → ❌ unhashable
```

---

# 18. Decorator + `lru_cache`

You solved an important interview-style question:

```python
@log_call
@lru_cache
def square(n):
    ...
```

This means:

```text
log_call(lru_cache(square))
```

The structure is:

```text
square()
   ↓
log_call wrapper
   ↓
"Calling"
   ↓
lru_cache
   ↓
cached result / original function
```

Therefore:

```python
square(5)
square(5)
```

produces:

```text
Calling
Calculating
25
Calling
25
```

### Why?

`log_call` is the **outer decorator**, so it runs every time.

`lru_cache` is inside it, so the actual calculation happens only when the result isn't cached.

---

# 19. Decorator Order Matters ⭐

Compare:

```python
@log_call
@lru_cache
def square():
    ...
```

with:

```python
@lru_cache
@log_call
def square():
    ...
```

They are **not equivalent**.

Because:

```text
@A
@B
```

means:

```python
A(B(function))
```

The outer decorator sees every call, while an inner caching decorator can prevent deeper execution.

This is an important interview concept.

---

# 20. Function Metadata vs Function Behavior

Keep these two ideas separate:

### Behavior

What the function **does**:

```python
return a + b
```

### Metadata

Information **about the function**:

```python
__name__
__doc__
```

`@wraps` primarily helps preserve the metadata when using decorators.

---

# 🧠 L17 One-Sheet

```text
FUNCTION DEEP DIVE
│
├── Closures
│   └── inner remembers enclosing variables
│
├── nonlocal
│   └── modify nearest enclosing function variable
│
├── Decorators
│   └── function → decorator → wrapper
│
├── @syntax
│   └── @dec → func = dec(func)
│
├── *args / **kwargs
│   ├── positional
│   └── keyword arguments
│
├── return
│   └── calculation ≠ return
│
├── wraps
│   └── preserve function metadata
│
├── Multiple decorators
│   ├── decoration: bottom → top
│   └── execution: outer → inner
│
├── Parameterized decorators
│   └── repeat(3)
│       ├── configuration
│       ├── decorator
│       └── wrapper
│
└── functools
    ├── wraps     → metadata
    ├── partial   → pre-fill arguments
    ├── reduce    → combine → ONE result
    └── lru_cache → cache function results
```

## 🎯 The most important connections from L17

```text
Closure
   ↓
remembers variables

Decorator
   ↓
uses functions to modify functions

Parameterized decorator
   ↓
uses closure + decorator together

wraps
   ↓
preserves function metadata

partial
   ↓
pre-fills function arguments

reduce
   ↓
accumulator → ONE result

lru_cache
   ↓
arguments → cache key → reuse result
```

**L17 is now complete.** ✅

Next according to your fixed roadmap: **L18 — OOP**, starting with **Classes → Objects → `__init__`**.

