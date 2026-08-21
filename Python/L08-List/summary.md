# Lesson 8 — Lists 🐍

### 1. Core concept

| Concept             | Remember                             |
| ------------------- | ------------------------------------ |
| `y = x`             | Same object / alias                  |
| `x.copy()` / `x[:]` | New outer list, shared inner objects |
| `deepcopy(x)`       | New outer + nested objects           |
| Mutable             | Existing list can change             |
| `x + y`             | New list                             |
| `x += y`            | Modifies existing list               |

### 2. Methods you confuse easily

| Pair          | Difference                           |
| ------------- | ------------------------------------ |
| `append(x)`   | Add **one object**                   |
| `extend(x)`   | Add **elements**                     |
| `pop(i)`      | Remove **by index**, returns value   |
| `remove(x)`   | Remove **by value**, returns `None`  |
| `del x[i]`    | Delete by index, returns nothing     |
| `clear()`     | Empty existing list                  |
| `sort()`      | Sort **in-place**, returns `None`    |
| `sorted(x)`   | Returns **new sorted list**          |
| `reverse()`   | Reverse **in-place**, returns `None` |
| `reversed(x)` | Returns **iterator**, doesn't modify |

### 3. Search vs direct access

| Operation    | Meaning             | Complexity |
| ------------ | ------------------- | ---------: |
| `x[i]`       | Index → value       |       O(1) |
| `x.index(v)` | Value → first index |       O(n) |
| `v in x`     | Does value exist?   |       O(n) |
| `x.count(v)` | How many?           |       O(n) |
| `len(x)`     | Number of items     |       O(1) |

### 4. Complexity to remember

| O(1)       | O(n)        | O(n log n) |
| ---------- | ----------- | ---------- |
| Index      | Search      | `sort()`   |
| `len()`    | `remove()`  | `sorted()` |
| `append()` | `insert(0)` |            |
| `pop()`    | `pop(0)`    |            |
|            | `count()`   |            |
|            | `reverse()` |            |

### 5. Nested-list trap ⭐

```python
[[0] * 3] * 3
```

→ **same inner list shared**

```python
[[0] * 3 for _ in range(3)]
```

→ **new inner list each time**

Think:

> `*` repeats references; comprehension creates new objects.

### 6. Comprehension / zip / enumerate

```python
[n*2 for n in x if n > 2]
```

→ creates a **new list**, usually O(n).

```python
enumerate(x)
```

→ `(index, value)`

```python
zip(a, b)
```

→ pairs corresponding elements; stops at shortest.

### 7. Unpacking

```python
a, *b, c = [1,2,3,4]
```

→

```text
a = 1
b = [2,3]
c = 4
```

**Starred variable always gets a list.**

### 8. Tiny memory hooks

> **append = one**
> **extend = many**

> **pop = index + returns**
> **remove = value**

> **sort/reverse = modify**
> **sorted/reversed = don't modify**

> **copy = shallow**
> **deepcopy = deep**

> **+ = new**
> **+= = in-place**

> **index = position**
> **in = existence**
> **count = quantity**

That's the version worth revisiting before moving on.






Yes. **Lesson 8 is done.** And your reason for asking this is valid: the concepts are understood, but several pairs are easy to mix up (`sort/sorted`, `reverse/reversed`, `+/+=`, `copy/deepcopy`, `append/extend`, `clear/del`).

Here is a **Lesson 8 revision sheet** designed specifically for revisiting later.

# Lesson 8 — Python Lists: Complete Revision Sheet

## 1. The core idea

| Concept          | Meaning                                  | Remember                   |
| ---------------- | ---------------------------------------- | -------------------------- |
| **List**         | Ordered, mutable collection              | List can be changed        |
| **Mutable**      | Existing object can be modified          | `x.append(10)` changes `x` |
| **Aliasing**     | Two names point to the same object       | `y = x`                    |
| **Rebinding**    | A name starts pointing to another object | `x = x + [10]`             |
| **Shallow copy** | New outer object, inner objects shared   | `x.copy()`, `x[:]`         |
| **Deep copy**    | Nested objects copied recursively        | `copy.deepcopy(x)`         |

### The most important question

Whenever you're confused, ask:

> **"Did we modify the existing object, or create a new object?"**

That single question explains most of Lesson 8.

---

# 2. Aliasing vs copying

Suppose:

```python
x = [1, 2, 3]
```

| Code                   | New list? | Same object? | Effect       |
| ---------------------- | --------: | -----------: | ------------ |
| `y = x`                |         ❌ |            ✅ | Alias        |
| `y = x.copy()`         |         ✅ |            ❌ | Shallow copy |
| `y = x[:]`             |         ✅ |            ❌ | Shallow copy |
| `y = list(x)`          |         ✅ |            ❌ | Shallow copy |
| `y = copy.deepcopy(x)` |         ✅ |            ❌ | Deep copy    |

For nested lists:

```python
x = [[1, 2], [3, 4]]
y = x.copy()
```

```text
x ──► [ ──► [1,2], ──► [3,4] ]
y ──► [ ──► [1,2], ──► [3,4] ]
             ↑           ↑
          shared      shared
```

Therefore:

```python
x is y        # False
x[0] is y[0]  # True
```

### Deep copy

```python
y = copy.deepcopy(x)
```

Now the inner objects aren't shared either.

```python
x[0] is y[0]  # False
```

---

# 3. `append()` vs `extend()`

|                    | `append()`         | `extend()`                        |
| ------------------ | ------------------ | --------------------------------- |
| Purpose            | Add **one object** | Add elements from an **iterable** |
| Example            | `x.append([3,4])`  | `x.extend([3,4])`                 |
| Result             | `[1,2,[3,4]]`      | `[1,2,3,4]`                       |
| Modifies original? | ✅                  | ✅                                 |
| Return value       | `None`             | `None`                            |
| Complexity         | O(1) amortized     | O(k) amortized                    |

### Important trap

```python
x.append("AB")
```

→

```text
[1, 2, "AB"]
```

But:

```python
x.extend("AB")
```

→

```text
[1, 2, "A", "B"]
```

Because strings are iterable.

### Memory rule

> **append = add this object**
> **extend = add the contents**

---

# 4. `+` vs `+=`

This one is extremely important.

|                         | `+`         | `+=` for lists |
| ----------------------- | ----------- | -------------- |
| Creates new list?       | ✅           | Usually ❌      |
| Modifies existing list? | ❌           | ✅              |
| Similar to              | —           | `extend()`     |
| Aliases see mutation?   | ❌           | ✅              |
| Example                 | `x = x + y` | `x += y`       |

Example:

```python
x = [1, 2]
y = x

x = x + [3]
```

Result:

```text
x → [1,2,3]
y → [1,2]
x is y → False
```

But:

```python
x = [1, 2]
y = x

x += [3]
```

Result:

```text
x → [1,2,3]
y → [1,2,3]
x is y → True
```

### Memory rule

> **`+` → new object**
> **`+=` → in-place for lists**

---

# 5. `sort()` vs `sorted()`

|                    | `sort()`    | `sorted()`        |
| ------------------ | ----------- | ----------------- |
| Belongs to         | List method | Built-in function |
| Modifies original? | ✅           | ❌                 |
| Returns            | `None`      | New list          |
| New list created?  | ❌           | ✅                 |
| Complexity         | O(n log n)  | O(n log n)        |

Example:

```python
x = [30, 10, 20]

x.sort()
```

`x` becomes:

```text
[10,20,30]
```

But:

```python
x = [30, 10, 20]
y = sorted(x)
```

gives:

```text
x → [30,10,20]
y → [10,20,30]
```

### Memory rule

> **sort = change the list**
> **sorted = give me a sorted list**

---

# 6. `reverse()` vs `reversed()`

This pair has exactly the same pattern.

|                       | `reverse()` | `reversed()`        |
| --------------------- | ----------- | ------------------- |
| Type                  | List method | Built-in            |
| Modifies original?    | ✅           | ❌                   |
| Returns               | `None`      | Iterator            |
| New list immediately? | ❌           | ❌                   |
| To get a list         | —           | `list(reversed(x))` |
| Complexity            | O(n)        | O(n) to consume     |

Example:

```python
x = [1,2,3]

x.reverse()
```

→

```text
x = [3,2,1]
```

But:

```python
x = [1,2,3]

y = reversed(x)
```

`x` stays:

```text
[1,2,3]
```

and:

```python
list(y)
```

gives:

```text
[3,2,1]
```

### Memory rule

> **reverse = modify**
> **reversed = iterator**

---

# 7. `clear()` vs `del`

|                         | `clear()` | `del x`                     |
| ----------------------- | --------- | --------------------------- |
| Removes elements?       | ✅         | ❌                           |
| Deletes variable name?  | ❌         | ✅                           |
| Existing list remains?  | ✅         | Depends on other references |
| Aliases see empty list? | ✅         | No                          |

Example:

```python
x = [1,2,3]
y = x

x.clear()
```

Both:

```text
x → []
y → []
```

But:

```python
x = [1,2,3]
y = x

del x
```

Now:

```text
x → doesn't exist
y → [1,2,3]
```

### Also remember

```python
del x[0]
```

deletes an element by index.

```python
del x[:]
```

empties the existing list.

### Memory rule

> **clear = empty the list**
> **del x = remove the name**

---

# 8. `pop()` vs `remove()` vs `del`

This trio is worth memorizing.

|                       | `pop()`               | `remove()`     | `del`                 |
| --------------------- | --------------------- | -------------- | --------------------- |
| Uses                  | Index                 | Value          | Index/slice/name      |
| Returns removed item? | ✅                     | ❌              | ❌                     |
| Example               | `x.pop(2)`            | `x.remove(30)` | `del x[2]`            |
| Search required?      | Usually no            | Yes            | No for direct index   |
| Complexity            | O(n) for middle/front | O(n)           | O(n) for middle/front |

### Example

```python
x = [10,20,30,40]
```

```python
x.pop(2)
```

→ removes **index 2** → `30`

and returns `30`.

```python
x.remove(30)
```

→ searches for **value 30** and removes the first occurrence.

```python
del x[2]
```

→ deletes **index 2**, returns nothing.

### Memory rule

> **pop → position + returns**
> **remove → value**
> **del → delete**

---

# 9. Indexing vs searching

| Operation        | What does it ask?             | Complexity |
| ---------------- | ----------------------------- | ---------: |
| `x[i]`           | Give me item at index `i`     |   **O(1)** |
| `x.index(value)` | Where is this value?          |   **O(n)** |
| `value in x`     | Does this value exist?        |   **O(n)** |
| `x.count(value)` | How many times does it exist? |   **O(n)** |

Why?

```python
x[5]
```

already knows exactly where to go.

But:

```python
30 in x
```

may need to search the whole list.

---

# 10. `in` vs `count()` vs `index()`

| Operation     | Question                | Can stop early? |
| ------------- | ----------------------- | --------------- |
| `30 in x`     | Does it exist?          | ✅               |
| `x.index(30)` | Where is the first one? | ✅               |
| `x.count(30)` | How many are there?     | ❌               |

All are worst-case:

```text
O(n)
```

---

# 11. `len()` vs `count()`

|            | `len()`                  | `count()`                  |
| ---------- | ------------------------ | -------------------------- |
| Question   | How many elements total? | How many equal this value? |
| Complexity | **O(1)**                 | **O(n)**                   |
| Why?       | List maintains its size  | Must inspect elements      |

```python
len([10,20,30])
```

→ `3`

```python
[10,20,10].count(10)
```

→ `2`

### Memory rule

> **len knows the size. count must search.**

---

# 12. Slicing

```python
x = [10,20,30,40,50]
```

```python
x[1:4]
```

→

```text
[20,30,40]
```

Slicing creates a **new list**.

If the slice contains `k` elements:

```text
Time → O(k)
```

Important:

```python
y = x[:]
```

is therefore a convenient **shallow copy**.

---

# 13. `reverse()` / `sort()` return `None`

Very common mistake:

```python
x = [3,1,2]

y = x.sort()
```

Now:

```text
y → None
x → [1,2,3]
```

Similarly:

```python
y = x.reverse()
```

→ `y` is `None`.

But:

```python
y = sorted(x)
```

→ `y` is the new sorted list.

And:

```python
y = list(reversed(x))
```

→ `y` is a new list.

---

# 14. List comprehensions

General form:

```python
[expression for item in iterable if condition]
```

Example:

```python
y = [n * 2 for n in x if n % 2 == 0]
```

Think:

```text
for every n
    ↓
check condition
    ↓
if True → perform expression
    ↓
put result in new list
```

### Example

```python
x = [1,2,3,4,5,6]
y = [n*2 for n in x if n%2 == 0]
```

→

```text
[4,8,12]
```

For `n` input elements:

```text
Typical complexity → O(n)
```

Important distinction:

```text
condition checks → every input element
expression executions → only elements that pass
```

---

# 15. Nested list comprehensions

```python
x = [[1,2], [3,4], [5,6]]

y = [n for row in x for n in row]
```

→

```text
[1,2,3,4,5,6]
```

Equivalent to:

```python
for row in x:
    for n in row:
        ...
```

If:

* `r` = number of rows
* `c` = elements per row

then:

```text
O(r × c)
```

---

# 16. The famous nested-list trap

### ❌ Dangerous

```python
x = [[0] * 3] * 3
```

The inner list is created **once** and referenced three times.

Therefore:

```python
x[0][0] = 99
```

gives:

```text
[[99,0,0],
 [99,0,0],
 [99,0,0]]
```

because:

```python
x[0] is x[1]
```

→ `True`

### ✅ Safe

```python
x = [[0] * 3 for _ in range(3)]
```

Each iteration creates a new inner list.

```python
x[0] is x[1]
```

→ `False`

### Memory rule

> `*` repeats references.
> Comprehension creates a new object each iteration.

---

# 17. `enumerate()`

Instead of:

```python
for i in range(len(x)):
    print(i, x[i])
```

use:

```python
for i, value in enumerate(x):
    print(i, value)
```

Produces conceptually:

```text
(index, value)
```

Example:

```python
list(enumerate(["a","b","c"]))
```

conceptually:

```text
[(0,"a"), (1,"b"), (2,"c")]
```

With:

```python
enumerate(x, start=1)
```

you get:

```text
1 a
2 b
3 c
```

`start=1` changes the **counter**, not the actual list indexes.

Complexity when consuming all `n` elements:

```text
O(n)
```

---

# 18. `zip()`

Combines corresponding elements:

```python
x = [1,2,3]
y = ["a","b","c"]

list(zip(x,y))
```

→

```text
[(1,"a"), (2,"b"), (3,"c")] - tuple
```

### Important

`zip()` itself returns a **zip iterator**.

```python
zip(x,y)
```

is not a list and not a tuple.

### Different lengths

```python
list(zip([1,2,3], ["a"]))
```

→

```text
[(1,"a")]
```

> **`zip()` stops at the shortest iterable.**

Complexity when consuming `n` pairs:

```text
O(n)
```

---

# 19. Unpacking

```python
a, b, c = [10,20,30]
```

→

```text
a = 10
b = 20
c = 30
```

### Starred unpacking

```python
a, *b = [10,20,30,40]
```

→

```text
a = 10
b = [20,30,40]
```

Important:

> The starred variable receives a **list**, not a tuple.

Example:

```python
a, *b, c = [10,20,30,40,50]
```

→

```text
a = 10
b = [20,30,40]
c = 50
```

---

# 20. `any()` vs `all()`

| Function | Meaning                | Early stopping?       | Worst case |
| -------- | ---------------------- | --------------------- | ---------: |
| `any()`  | At least one is truthy | Yes, at first `True`  |       O(n) |
| `all()`  | Everything is truthy   | Yes, at first `False` |       O(n) |

Example:

```python
any([False, False, True])
```

→ `True`

```python
all([True, True, False])
```

→ `False`

---

# 21. `min()`, `max()`, `sum()`

| Function | Purpose  | Complexity |
| -------- | -------- | ---------: |
| `min(x)` | Smallest |       O(n) |
| `max(x)` | Largest  |       O(n) |
| `sum(x)` | Total    |       O(n) |

They need to inspect the elements.

---

# 22. Master complexity table

This is the table I'd **actually save for revision**.

| Operation                 |          Complexity | Main reason        |
| ------------------------- | ------------------: | ------------------ |
| `x[i]`                    |            **O(1)** | Direct index       |
| `len(x)`                  |            **O(1)** | Size is maintained |
| `append()`                |  **O(1)** amortized | Add at end         |
| `pop()`                   |            **O(1)** | Remove last        |
| `insert(0, x)`            |            **O(n)** | Shift elements     |
| `pop(0)`                  |            **O(n)** | Shift elements     |
| `remove(x)`               |            **O(n)** | Search + remove    |
| `x[i] = value`            |            **O(1)** | Direct index       |
| `x[i:j]`                  |            **O(k)** | Copy `k` elements  |
| `x.copy()`                |            **O(n)** | Copy outer list    |
| `x[:]`                    |            **O(n)** | Copy slice         |
| `value in x`              |            **O(n)** | Search             |
| `x.index(value)`          |            **O(n)** | Search             |
| `x.count(value)`          |            **O(n)** | Full scan          |
| `x.reverse()`             |            **O(n)** | Reverse elements   |
| `reversed(x)`             | **O(n)** to consume | Traverse backwards |
| `x.sort()`                |      **O(n log n)** | Sorting            |
| `sorted(x)`               |      **O(n log n)** | Sorting + new list |
| `x + y`                   |        **O(n + m)** | Copy both          |
| `x.extend(y)`             |  **O(m)** amortized | Add `m` elements   |
| list comprehension        |    **O(n)** typical | Process elements   |
| `zip()` consumption       |            **O(n)** | Process pairs      |
| `enumerate()` consumption |            **O(n)** | Process elements   |
| `min()`                   |            **O(n)** | Scan               |
| `max()`                   |            **O(n)** | Scan               |
| `sum()`                   |            **O(n)** | Scan               |
| `any()`                   | **O(n)** worst case | May stop early     |
| `all()`                   | **O(n)** worst case | May stop early     |

---

# 23. The "confusing pairs" cheat sheet

This is probably the most useful part for you.

| Pair                       | First one                 | Second one                |
| -------------------------- | ------------------------- | ------------------------- |
| `sort()` / `sorted()`      | **modifies**              | **new sorted list**       |
| `reverse()` / `reversed()` | **modifies**              | **reverse iterator**      |
| `+` / `+=`                 | **new list**              | **in-place for lists**    |
| `append()` / `extend()`    | **one object**            | **elements of iterable**  |
| `copy()` / `deepcopy()`    | **shared nested objects** | **copies nested objects** |
| `clear()` / `del x`        | **empty list**            | **delete name**           |
| `pop()` / `remove()`       | **by index**              | **by value**              |
| `in` / `count()`           | **exists?**               | **how many?**             |
| `x[i]` / `x.index(v)`      | **index → value**         | **value → index**         |
| `reverse()` / `sort()`     | **change order**          | **arrange by value**      |

---

# 24. The 10 rules I'd memorize

If you don't want to memorize the entire lesson, remember these:

```text
1. List = mutable.

2. y = x
   → same object.

3. copy / [:]
   → new outer list, shared nested objects.

4. deepcopy
   → recursively copies nested objects.

5. append
   → one object.

6. extend
   → elements from iterable.

7. + 
   → new list.

8. +=
   → in-place for lists.

9. sort/reverse
   → modify list, return None.

10. sorted/reversed
    → don't modify original.
```

And the complexity anchors:

```text
O(1) → index, len, append, pop-last

O(n) → search, remove, insert-front, pop-front,
       count, reverse, comprehension

O(n log n) → sort / sorted
```

That is the **Lesson 8 reference sheet** I'd use when revisiting. You don't need to memorize every explanation; use the tables to quickly reconstruct the concept.
