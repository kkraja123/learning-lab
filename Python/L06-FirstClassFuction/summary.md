# 📘 Lesson 6 Summary – First-Class Functions, Closures & Decorators

## 🎯 Goal

Understand how Python treats **functions as objects**, how **closures** work internally, and how **decorators** are built from first principles.

---

# 1. Functions are Objects

A `def` statement creates a **function object**.

```python
def greet():
    print("Hello")
```

Memory:

```text
greet ─────► Function Object
```

A function is an object like:

* Integer object
* String object
* List object
* Class object

---

# 2. Functions are First-Class Objects

A function object can be:

### Assigned

```python
x = greet
```

Both names point to the same function object.

---

### Passed as an argument

```python
process(greet)
```

The parameter is bound to the **same function object**.

---

### Returned

```python
return greet
```

Returns the function object.

Not:

```python
return greet()
```

---

# 3. Higher-Order Functions

A function that:

* accepts another function
* returns another function

is called a **Higher-Order Function**.

Example:

```python
process(greet)
```

---

# 4. Nested Functions

Functions can be defined inside another function.

```python
def outer():

    def inner():
        pass
```

Important:

`inner` is **NOT** created when Python reads the file.

It is created **only when `outer()` executes**.

---

# 5. Closures

A closure remembers the **enclosing environment**.

Example:

```python
def outer():

    count = 10

    def inner():
        print(count)

    return inner
```

The closure **does not copy** the value.

Instead it remembers the **binding** to the enclosing variable.

Mental model:

```text
Function Object
        │
        ▼
Closure
        │
        ▼
Enclosing Environment
        │
        ▼
count ─────► Integer Object
```

---

# 6. Closures Keep Variables Alive

Normally:

Local variables disappear after a function returns.

But if a closure references them:

Python keeps the enclosing environment alive.

---

# 7. Decorators (Built Manually)

We built decorators ourselves.

Not by memorizing.

Started with:

```python
login = decorate(login)
```

Then understood that

```python
@decorate
```

is simply syntactic sugar for

```python
login = decorate(login)
```

---

# 8. Decorator Structure

We derived:

```python
def decorate(func):

    def wrapper(*args, **kwargs):

        print("Starting...")

        result = func(*args, **kwargs)

        print("Finished...")

        return result

    return wrapper
```

Every line has a purpose.

---

# 9. `*args`

Collects positional arguments into a tuple.

```python
def func(*args):
```

Example:

```python
func(10,20,30)

args == (10,20,30)
```

---

# 10. `**kwargs`

Collects keyword arguments into a dictionary.

```python
def func(**kwargs):
```

Example:

```python
func(name="Karthick")
```

Inside:

```python
kwargs

{
    "name":"Karthick"
}
```

---

# 11. Unpacking

Tuple:

```python
func(*args)
```

becomes

```python
func(10,20)
```

Dictionary:

```python
func(**kwargs)
```

becomes

```python
func(name="Karthick")
```

---

# 12. Return Values in Decorators

Wrong:

```python
func(*args)
```

Correct:

```python
result = func(*args, **kwargs)

return result
```

Otherwise the wrapper returns:

```python
None
```

---

# 13. `@wraps`

Without:

```python
login.__name__
```

prints

```text
wrapper
```

With:

```python
@wraps(func)
```

Metadata is copied.

Now

```python
login.__name__
```

prints

```text
login
```

---

# 🧠 Mental Models to Remember

## Function Object

```text
def
    │
    ▼
Function Object
```

---

## Passing Function

```text
greet
   │
   ▼
Function Object
   ▲
   │
func
```

---

## Returning Function

```text
return inner

returns

Function Object
```

---

## Closure

```text
Function Object
        │
        ▼
Closure
        │
        ▼
Enclosing Environment
        │
        ▼
Variables
```

---

## Decorator

```text
login
   │
   ▼
Wrapper Function
      │
      ▼
Closure
      │
      ▼
Original login()
```

---

# ⭐ Lesson 6 Outcome

After this lesson, you can confidently explain:

* ✅ Functions are objects.
* ✅ Functions can be assigned, passed, and returned.
* ✅ What a higher-order function is.
* ✅ When nested functions are created.
* ✅ How closures keep variables alive.
* ✅ How decorators work internally.
* ✅ Why `*args` and `**kwargs` are needed.
* ✅ Why `@wraps` exists.

---
