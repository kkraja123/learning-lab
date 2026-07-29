# Lesson 5 — Python Object Model

> **Core Idea:** Everything in Python is an object.

---

# 5.1 Variables are Names

Variables **do not store objects**.

They are **names bound to objects**.

```python
x = 10
y = x
```

```text
x ─────► 10

y ─────► 10
```

**Remember**

* Assignment never copies an object.
* Assignment binds another name.

---

# 5.2 Everything is an Object

Everything is an object.

| Expression | Object            |
| ---------- | ----------------- |
| `10`       | Integer object    |
| `"Hello"`  | String object     |
| `[]`       | List object       |
| `{}`       | Dictionary object |
| `print`    | Function object   |
| `Student`  | Class object      |

---

# 5.3 Class Object vs Instance Object

```python
class Student:
    pass
```

Python creates **one class object**.

```text
Student
   │
   ▼
Class Object
```

When you do:

```python
s = Student()
```

Python creates a **Student instance**.

```text
Student ─────► Class Object

s ───────────► Student Instance
```

---

# 5.4 `type()`

Every object has a type.

Examples:

| Expression        | Result    |
| ----------------- | --------- |
| `type(10)`        | `int`     |
| `type("abc")`     | `str`     |
| `type([])`        | `list`    |
| `type(Student)`   | `type`    |
| `type(Student())` | `Student` |

---

# 5.5 Class Objects

These are all class objects.

```python
int
str
list
dict
set
tuple
Student
```

Their type:

```python
type(list)
```

↓

```python
<class 'type'>
```

Because every class object is created by `type`.

---

# 5.6 Function Objects

Built-in functions

```python
print
len
sum
```

User-defined

```python
def greet():
    pass
```

`greet` is also an object.

---

# 5.7 Built-in vs User-defined Functions

| Object  | Type                         |
| ------- | ---------------------------- |
| `print` | `builtin_function_or_method` |
| `len`   | `builtin_function_or_method` |
| `greet` | `function`                   |

---

# 5.8 Truthiness Protocol

Python evaluates truthiness like this:

```text
if obj
      │
      ▼
Has __bool__() ?
      │
      ├── Yes → Use it
      │
      └── No
             │
             ▼
      Has __len__() ?
             │
             ├── len == 0 → False
             └── len > 0 → True

Otherwise → True
```

Examples:

```python
[]
```

↓

False

```python
""
```

↓

False

```python
[1]
```

↓

True

---

# 5.9 `len()` Protocol

Python doesn't hardcode list length.

Instead:

```python
len(obj)
```

Conceptually becomes

```python
obj.__len__()
```

---

# 5.10 `()` Means Call

This was the biggest lesson.

Python **does not ask**

* Is this a class?
* Is this a function?

Python asks

```text
Is this object callable?
```

---

# 5.11 `__call__()`

```python
class Dog:
    def __call__(self):
        print("Woof")
```

```python
d = Dog()

d()
```

Conceptually

```text
d()
 │
 ▼
Is object callable?
 │
 ▼
d.__call__()
```

---

# 5.12 Python's General Design

Python converts syntax into special methods.

| Syntax     | Special Method |
| ---------- | -------------- |
| `len(obj)` | `__len__()`    |
| `if obj:`  | `__bool__()`   |
| `obj()`    | `__call__()`   |

Later you'll learn more:

| Syntax               | Special Method  |
| -------------------- | --------------- |
| `obj[index]`         | `__getitem__()` |
| `obj[index] = value` | `__setitem__()` |
| `obj1 + obj2`        | `__add__()`     |
| `for x in obj`       | `__iter__()`    |
| `next(obj)`          | `__next__()`    |

---

# Memory Table

| Expression  | Kind of Object               | `type(...)`                  |
| ----------- | ---------------------------- | ---------------------------- |
| `10`        | Integer instance             | `int`                        |
| `"Hello"`   | String instance              | `str`                        |
| `[]`        | List instance                | `list`                       |
| `{}`        | Dictionary instance          | `dict`                       |
| `Student`   | Class object                 | `type`                       |
| `Student()` | Student instance             | `Student`                    |
| `list`      | Class object                 | `type`                       |
| `list()`    | List instance                | `list`                       |
| `print`     | Built-in function object     | `builtin_function_or_method` |
| `len`       | Built-in function object     | `builtin_function_or_method` |
| `greet`     | User-defined function object | `function`                   |

---

# Three Golden Rules ⭐

### Rule 1

Without `()`, you're referring to an object.

```python
Student
list
print
10
```

---

### Rule 2

With `()`, you're asking Python to **call** an object.

```python
Student()
list()
print()
greet()
```

Python checks:

> **Is this object callable?**

---

### Rule 3

`type(x)` tells you **what kind of object** `x` is.

---

# Mental Model (Most Important)

```text
Everything is an Object
          │
          ▼
Every Object Has a Type
          │
          ▼
Some Objects Are Callable
          │
          ▼
Python Uses Special Methods
          │
          ▼
Language Syntax Works
```

This is the mental model to keep in your head. Once it's solid, advanced topics like decorators, iterators, context managers, descriptors, and metaclasses become much easier because they all build on this same foundation.
