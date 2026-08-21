Lesson Objectives

By the end of this lesson, you'll understand:

What a string really is.
Why strings are immutable.
How Python stores strings internally.
String indexing.
String slicing.
String interning.
Common string operations.
Time complexity of string operations.
Common interview questions.


1. Searching (O(n))
✅ find()
index()
startswith()
endswith()
count()
2. Modifying (O(n))
✅ replace()
strip()
lstrip()
rstrip()
3. Splitting & Joining (Very important for DSA)
split()
splitlines()
join() ⭐⭐⭐⭐⭐
4. Checking (O(n))
isalpha()
isdigit()
isalnum()
islower()
isupper()
isspace()


> **Important:** For complexity, `n` = string length and `m` = length of the searched prefix/suffix/pattern where applicable. Some CPython implementation details can vary, but these are the useful interview-level complexities.

## 🧠 Python String Methods — Master Table

| Method                        | What it does / Rule                                        | Hint to remember                        | Important edge case                       |         Time | Space |
| ----------------------------- | ---------------------------------------------------------- | --------------------------------------- | ----------------------------------------- | -----------: | ----: |
| `s.upper()`                   | Converts cased characters to uppercase                     | **New string**                          | `"123".upper()` → `"123"`                 |         O(n) |  O(n) |
| `s.lower()`                   | Converts cased characters to lowercase                     | **New string**                          | `"123".lower()` → `"123"`                 |         O(n) |  O(n) |
| `s.capitalize()`              | First character uppercase, remaining cased chars lowercase | **First char only**                     | `"pYTHON"` → `"Python"`                   |         O(n) |  O(n) |
| `s.replace(old, new)`         | Replaces occurrences of `old`                              | **All matching occurrences by default** | `replace("", "-")` has special behavior   | O(n) typical |  O(n) |
| `s.find(sub)`                 | First occurrence index                                     | **Not found → `-1`**                    | `find("")` → `0`                          |         O(n) |  O(1) |
| `s.index(sub)`                | First occurrence index                                     | **Like `find`, but raises error**       | Not found → `ValueError`                  |         O(n) |  O(1) |
| `s.count(sub)`                | Counts non-overlapping occurrences                         | **Count, don't search manually**        | `count("")` → `n+1`                       |         O(n) |  O(1) |
| `s.split()`                   | Splits using whitespace                                    | **No argument = whitespace**            | Multiple whitespace treated as separator  |         O(n) |  O(n) |
| `s.split(",")`                | Splits using exact separator                               | **Empty fields preserved**              | `"a,,b".split(",")` → `["a","","b"]`      |         O(n) |  O(n) |
| `sep.join(iterable)`          | Combines strings using separator                           | **List → String**                       | Elements must be strings                  |         O(n) |  O(n) |
| `s.strip()`                   | Removes whitespace from both ends                          | **Edges only**                          | Doesn't touch middle                      |         O(n) |  O(n) |
| `s.lstrip()`                  | Removes whitespace from left                               | **L = Left**                            | Middle/right untouched                    |         O(n) |  O(n) |
| `s.rstrip()`                  | Removes whitespace from right                              | **R = Right**                           | Middle/left untouched                     |         O(n) |  O(n) |
| `s.strip(chars)`              | Removes characters from both ends that belong to `chars`   | **Character set, NOT substring**        | `"abcXcba".strip("abc")` → `"X"`          |         O(n) |  O(n) |
| `s.startswith(prefix)`        | Checks beginning                                           | **Prefix**                              | `startswith("")` → `True`                 |         O(m) |  O(1) |
| `s.endswith(suffix)`          | Checks ending                                              | **Suffix**                              | `endswith("")` → `True`                   |         O(m) |  O(1) |
| `s.startswith(p, start)`      | Checks prefix beginning at `start`                         | **Start index**                         | Doesn't create a slice                    |         O(m) |  O(1) |
| `s.startswith(p, start, end)` | Checks within `[start:end]`                                | **End excluded**                        | Same slicing boundary concept             |         O(m) |  O(1) |
| `s.isalpha()`                 | All characters alphabetic                                  | **At least 1 + all letters**            | `""` → `False`                            |         O(n) |  O(1) |
| `s.isdigit()`                 | All characters are digits                                  | **Character test, not number parsing**  | `"-123"` → `False`                        |         O(n) |  O(1) |
| `s.isdecimal()`               | All characters are decimal digits                          | **Strictest numeric test**              | `"12.5"` → `False`                        |         O(n) |  O(1) |
| `s.isnumeric()`               | All characters have numeric meaning                        | **Broadest numeric test**               | `"½"` → `True`                            |         O(n) |  O(1) |
| `s.isalnum()`                 | All characters are alphabetic **OR** numeric               | **OR, not AND**                         | `"Python"` → `True`; `"123"` → `True`     |         O(n) |  O(1) |
| `s.islower()`                 | Has cased chars and all are lowercase                      | **Uncased chars ignored**               | `"python123"` → `True`; `"123"` → `False` |         O(n) |  O(1) |
| `s.isupper()`                 | Has cased chars and all are uppercase                      | **Uncased chars ignored**               | `"PYTHON123"` → `True`; `"123"` → `False` |         O(n) |  O(1) |
| `s.isspace()`                 | Non-empty and every char is whitespace                     | **ALL must be whitespace**              | `"a b"` → `False`; `" \t"` → `True`       |         O(n) |  O(1) |

---

# ⭐ The Rules You REALLY Need to Remember

Instead of memorizing 25 methods independently, group them.

### 1. Methods that create a new string

```python
upper()
lower()
capitalize()
replace()
strip()
lstrip()
rstrip()
```

Remember:

> **Strings are immutable → these cannot modify the original string.**

---

### 2. Methods that return information

```python
find()
index()
count()
startswith()
endswith()
```

They don't need to create a modified string.

---

### 3. Boolean checking methods

```python
isalpha()
isdigit()
isdecimal()
isnumeric()
isalnum()
islower()
isupper()
isspace()
```

Generally:

```text
Time  → O(n)
Space → O(1)
```

because they may scan the characters without creating another string.

---

# 🔥 Five Rules I Want You to NEVER Forget

### Rule 1 — `strip()` is NOT substring removal

```python
"abcPythoncba".strip("abc")
```

means:

> Remove any `a`, `b`, or `c` from the edges.

It does **not** mean:

> Remove `"abc"`.

---

### Rule 2 — `split()` vs `join()`

Think:

```text
String ──split()──> List
List ──join()─────> String
```

This pair is extremely important for DSA.

---

### Rule 3 — `+` vs `join()`

Repeated:

```python
result += word
```

can lead to **O(n²)** total copying because strings are immutable.

Prefer:

```python
"".join(words)
```

for assembling many strings → **O(n)**.

---

### Rule 4 — `is...()` methods don't convert anything

For example:

```python
"123".isdigit()
```

doesn't convert `"123"` to `123`.

It asks whether the characters satisfy the digit rule.

Similarly:

```python
"-123".isdigit()
```

→ `False`

because `-` is a character and isn't a digit.

---

### Rule 5 — Empty strings have special behavior

Remember these:

```python
"".startswith("")   # True
"".endswith("")     # True
"".find("")         # 0
"".count("")        # 1
"".isalpha()        # False
"".isdigit()        # False
"".isalnum()        # False
"".isspace()        # False
```

The checking methods generally require **at least one relevant character**.

---

# 🧠 Numeric Methods — One Mini Table

This was the confusing part, so keep this separately:

| Character | `isdecimal()` | `isdigit()` | `isnumeric()` |
| --------- | :-----------: | :---------: | :-----------: |
| `"3"`     |       ✅       |      ✅      |       ✅       |
| `"٣"`     |       ✅       |      ✅      |       ✅       |
| `"²"`     |       ❌       |      ✅      |       ✅       |
| `"½"`     |       ❌       |      ❌      |       ✅       |
| `"."`     |       ❌       |      ❌      |       ❌       |
| `"-"`     |       ❌       |      ❌      |       ❌       |

The key is:

> These methods inspect **characters**, not whether the whole string represents a mathematical number.

So:

```python
"12.5".isnumeric()
```

is `False`, because `.` is not a numeric character.

---

# 🎯 DSA Priority

If you're preparing for DSA, don't give every method equal importance.

### ⭐⭐⭐⭐⭐ Must know

```text
split()
join()
find()
count()
replace()
strip()
startswith()
endswith()
isdigit()
isalnum()
```

### ⭐⭐⭐ Useful

```text
upper()
lower()
isalpha()
islower()
isupper()
isspace()
```

### ⭐ Mostly knowledge

```text
isdecimal()
isnumeric()
```

---

Now we have a solid reference. **Let's continue with string interning**, because it connects directly to the object identity concepts you learned earlier.
