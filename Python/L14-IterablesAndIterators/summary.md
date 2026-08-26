# L10 — Iterables & Iterators 🐍

### Iterable

An object that can provide an iterator.

Examples:

```python
list
tuple
str
dict
set
```

### Iterator

An object that produces values **one at a time** and maintains its current state.

```python
numbers = [10, 20, 30]

it = iter(numbers)

next(it)  # 10
next(it)  # 20
next(it)  # 30
```

### Core protocol

```text
Iterable
   ↓ iter()
Iterator
   ↓ next()
Value
   ↓
StopIteration
```

### Important rules 🔒

* `iter(obj)` → gets an iterator.
* `next(iterator)` → gets the next value.
* `StopIteration` → no more values.
* `for` internally uses `iter()` and `next()`.
* Iterators maintain **state**.
* An iterator is also an iterable.
* `iter(iterator) is iterator` → `True`.
* Every iterable is **not necessarily** an iterator.
* List → iterable, not iterator.
* `iter(list)` → list iterator.

### Key mental model

> **Iterable gives you an iterator; iterator gives you values.**

**L10 complete. ✅**
