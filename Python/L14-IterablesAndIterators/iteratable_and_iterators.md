1. What is an Iterable?

- An iterable is an object that can provide its elements one by one when Python asks for them.
- Iterable = something you can iterate over.

| Iterable                | Iterator                |
| ----------------------- | ----------------------- |
| Can provide an iterator | Produces the next value |
| `iter(obj)` works       | `next(obj)` works       |
| Example: `list`         | Example: `iter(list)`   |


Iterable
→ can give an iterator

Iterator
→ can give the next value

## Key rules:

- Iterable → can provide an iterator
- Iterator → produces values one at a time
- iter(obj) → obtains an iterator
- next(iterator) → gets the next value
- StopIteration → signals no more values
- for → internally uses this mechanism
- An iterator maintains state
- An iterator is also an iterable
- iter(iterator) is iterator → True
- A list is iterable but not an iterator

Two separate calls to iter(iterable) normally create separate iterators. But calling iter() on an iterator returns that same iterator.


Absolutely. **L10 is complete. ✅**
Here is the short-but-complete summary you can keep for revision.

# 🐍 L10 — Iterables & Iterators

## 1. Iterable

An **iterable** is an object that can provide its elements one by one.

Examples:

```python
list
tuple
string
set
dict
```

Example:

```python
numbers = [10, 20, 30]

for x in numbers:
    print(x)
```

A list is **iterable**, but it is not itself an iterator.

---

## 2. Iterator

An **iterator** is an object that:

* Produces values one at a time
* Maintains its current **state/position**
* Implements `__next__()`
* Is also iterable

```python
numbers = [10, 20, 30]

x = iter(numbers)
```

Now:

```text
numbers → iterable
x       → iterator
```

---

## 3. `iter()`

`iter()` obtains an iterator from an iterable.

```python
numbers = [10, 20, 30]

x = iter(numbers)
```

Conceptually:

```text
iterable
   ↓ iter()
iterator
```

---

## 4. `next()`

`next()` asks the iterator for its next value.

```python
x = iter([10, 20, 30])

next(x)  # 10
next(x)  # 20
next(x)  # 30
```

The iterator remembers its state.

---

## 5. `StopIteration`

When the iterator has no more values:

```python
next(x)
```

raises:

```text
StopIteration
```

It does **not** return `None`.

---

## 6. How `for` actually works 🔥

This:

```python
for x in numbers:
    print(x)
```

conceptually works like:

```python
iterator = iter(numbers)

while True:
    try:
        x = next(iterator)
        print(x)
    except StopIteration:
        break
```

So:

```text
for
 ↓
iter()
 ↓
iterator
 ↓
next()
 ↓
value
 ↓
next()
 ↓
StopIteration
 ↓
loop ends
```

---

## 7. `__iter__()` and `__next__()`

Two important special methods:

```text
__iter__() → returns an iterator
__next__() → returns the next value
```

Conceptually:

```python
iterator = obj.__iter__()
value = iterator.__next__()
```

---

## 8. Iterator is also iterable

This is a **very important rule**:

> **Every iterator is iterable, but not every iterable is an iterator.**

For an iterator:

```python
x = iter(numbers)

iter(x) is x
```

→ `True`

An iterator's `__iter__()` returns **itself**.

---

## 9. Separate iterators have separate state

```python
numbers = [10, 20, 30]

a = iter(numbers)
b = iter(numbers)
```

Here:

```text
a → separate iterator
b → separate iterator
```

So:

```python
next(a)  # 10
next(a)  # 20

next(b)  # 10
```

`a` and `b` don't share state.

---

## 10. `iter()` on an iterator

This is different:

```python
a = iter(numbers)
b = iter(a)
```

Because `a` is already an iterator:

```python
b is a
```

→ `True`

Therefore they **share the same state**.

---

# ⭐ L10 Cheat Sheet

```text
ITERABLE
    │
    │ iter()
    ↓
ITERATOR
    │
    │ next()
    ↓
VALUE
    │
    │ next()
    ↓
VALUE
    │
    │ no more values
    ↓
StopIteration
```

### Remember these 6 rules:

1. **List → iterable, not iterator**
2. **`iter()` → gets an iterator**
3. **`next()` → gets next value**
4. **Iterator remembers state**
5. **`StopIteration` → no more values**
6. **Every iterator is iterable, but not every iterable is an iterator**

### Most important interview statement

> **A `for` loop works by obtaining an iterator from the iterable and repeatedly calling `next()` until `StopIteration` occurs.**

**L10 complete. 🔒✅**

Next in our locked roadmap is **L15 — Comprehensions**, because **L11–L14 are already completed by you in the other chat.**
