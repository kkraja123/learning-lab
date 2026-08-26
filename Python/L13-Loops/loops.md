# while loop

while condition:
    # work
    # update condition-related state


# Range

range(stop)
→ starts at 0

range(start, stop)
→ starts at start, stops before stop

range(start, stop, step)
start → where to begin
stop  → where to stop (EXCLUDED)
step  → how much to move

break    → exit the entire loop
continue → skip current iteration

normal completion → else runs
break             → else skipped

break    → exits loop
continue → skips current iteration
loop else → runs only if loop finishes normally


for       → iterate over an iterable
while     → repeat while condition is truthy
range     → generates a sequence of numbers
break     → exit current loop
continue  → skip current iteration
loop else → runs only after normal completion
nested    → inner loop runs for each outer iteration


# L13 — Loops 🔄

## 1. `while` loop

Use `while` when repetition depends on a **condition**.

```python
count = 1

while count <= 3:
    print(count)
    count += 1
```

Execution:

```text
1 → 2 → 3 → condition becomes False → stop
```

### Important

A `while` loop needs a way for its condition to eventually become false.

```python
count = 1

while count <= 3:
    print(count)
```

This is an **infinite loop** because `count` never changes.

---

## 2. `for` loop

Use `for` when you want to iterate through an **iterable**.

```python
numbers = [10, 20, 30]

for number in numbers:
    print(number)
```

`number` receives each element:

```text
number → 10
number → 20
number → 30
```

It is **not automatically an index**.

---

## 3. Iterables

`for` can iterate over many types:

```text
list       → elements
tuple      → elements
string     → characters
set        → elements
dictionary → keys
```

Example:

```python
for char in "Python":
    print(char)
```

Output:

```text
P
y
t
h
o
n
```

---

## 4. Dictionary iteration

By default:

```python
for key in person:
    print(key)
```

iterates over **keys**.

For values:

```python
for value in person.values():
    print(value)
```

For both:

```python
for key, value in person.items():
    print(key, value)
```

---

# 5. `range()`

### `range(stop)`

Starts at `0` and stops **before** `stop`.

```python
range(5)
```

produces:

```text
0 1 2 3 4
```

### `range(start, stop)`

```python
range(2, 6)
```

produces:

```text
2 3 4 5
```

### `range(start, stop, step)`

```python
range(0, 10, 2)
```

produces:

```text
0 2 4 6 8
```

### Negative step

```python
range(5, 0, -1)
```

produces:

```text
5 4 3 2 1
```

### Core rule

```text
range(start, stop, step)

start → where to begin
stop  → excluded
step  → how much to move
```

---

# 6. `break`

`break` **exits the current loop completely**.

```python
for i in range(5):
    if i == 3:
        break
    print(i)
```

Output:

```text
0
1
2
```

When `i == 3`, the loop immediately ends.

---

# 7. `continue`

`continue` **skips the current iteration** and moves to the next iteration.

```python
for i in range(5):
    if i == 3:
        continue
    print(i)
```

Output:

```text
0
1
2
4
```

### Remember

```text
break    → exit loop
continue → skip current iteration
```

---

# 8. `for...else`

Python allows an `else` after a loop.

```python
for i in range(3):
    print(i)
else:
    print("Done")
```

Output:

```text
0
1
2
Done
```

The loop `else` runs when the loop **finishes normally**.

If `break` happens:

```python
for i in range(3):
    if i == 1:
        break
else:
    print("Done")
```

`Done` is **not printed**.

### Rule 🔒

```text
Normal loop completion → else runs
break                  → else skipped
```

---

# 9. Nested loops

A loop inside another loop:

```python
for i in range(2):
    for j in range(2):
        print(i, j)
```

Output:

```text
0 0
0 1
1 0
1 1
```

The inner loop runs completely for **each iteration of the outer loop**.

If:

```text
outer = 3 iterations
inner = 2 iterations
```

Then:

```text
3 × 2 = 6
```

executions.

### Complexity connection

When both loops depend on `n`:

```text
O(n²)
```

---

# 10. `break` inside nested loops

Important:

```python
for i in range(3):
    for j in range(3):
        if j == 1:
            break
```

The `break` exits **only the inner loop**.

The outer loop continues.

```text
i = 0 → inner breaks
i = 1 → inner breaks
i = 2 → inner breaks
```

### Rule

> `break` affects the **nearest loop containing it**.

---

# 11. `continue` inside nested loops

```python
for i in range(3):
    for j in range(3):
        if j == 1:
            continue
        print(i, j)
```

`continue` skips only that particular **inner-loop iteration**.

Output:

```text
0 0
0 2
1 0
1 2
2 0
2 2
```

---

# 12. Choosing `for` vs `while`

### Use `for`

When you have an iterable or a known sequence of values:

```python
for number in numbers:
    ...
```

Example:

> Process every item in a list.

### Use `while`

When repetition depends on a condition and you don't necessarily know the number of iterations beforehand:

```python
while password != correct_password:
    ...
```

Example:

> Keep asking until the correct password is entered.

### Mental model

```text
Iterable / sequence → for
Condition-driven repetition → while
```

---

# 13. Loop execution order

For:

```python
for i in range(3):
    print(i)
```

think:

```text
get next value
     ↓
assign to i
     ↓
execute body
     ↓
get next value
     ↓
...
```

For `while`:

```python
while condition:
    body
```

think:

```text
check condition
     ↓
True?
 ↓       ↓
yes      no
 ↓       ↓
body    STOP
 ↓
check again
```

---

# 14. L13 Mental Cheat Sheet 🧠

```text
while
→ repeat while condition is truthy

for
→ iterate through an iterable

range
→ generates numbers
→ stop value is excluded

break
→ exit current loop

continue
→ skip current iteration

for...else
→ else runs if no break occurred

nested loop
→ inner loop runs for every outer iteration

nested break
→ exits nearest/current loop only

nested continue
→ skips nearest/current loop iteration

for vs while
→ iterable/sequence → for
→ condition-driven → while
```

## ⭐ Most important L13 rules

If you remember only these, you're in good shape:

```text
1. range() excludes stop.
2. break exits the current loop.
3. continue skips the current iteration.
4. for...else runs else only when there was no break.
5. Nested inner loops run completely for each outer iteration.
6. A while loop must eventually make its condition false.
7. for is naturally used for iterables.
```

**L13 complete. ✅**
