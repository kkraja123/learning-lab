## L13 — Loops: Short Summary

### `while`

Repeats **while a condition is truthy**.

```python
while condition:
    ...
```

### `for`

Iterates over an **iterable**, one value at a time.

```python
for x in items:
    ...
```

### `range()`

```text
range(stop)           → 0 to stop-1
range(start, stop)    → start to stop-1
range(start, stop, step)
```

`stop` is always **excluded**.

### `break`

**Exits the current loop completely.**

### `continue`

**Skips the current iteration** and moves to the next one.

### `for...else`

```python
for x in items:
    ...
else:
    ...
```

`else` runs only when the loop **finishes normally** — not when `break` occurs.

### Nested loops

```python
for i in ...:
    for j in ...:
```

The inner loop runs completely for each outer iteration.

**Key rule:**

> `for` → iterate over something
> `while` → repeat until a condition changes
> `break` → exit
> `continue` → skip one iteration

**L13 complete. ✅**
