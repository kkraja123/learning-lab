# L15 — Comprehensions 🐍

### List

```python
[x * 2 for x in numbers]
```

### Filtering

```python
[x for x in numbers if x > 2]
```

**False → skip**

### Conditional expression

```python
[x if x > 2 else 0 for x in numbers]
```

**False → use `else` value**

### Set

```python
{x * 2 for x in numbers}
```

Duplicates are removed.

### Dictionary

```python
{x: x * x for x in numbers}
```

Keys are unique; values can repeat.

### Nested

```python
[[x * 2 for x in row] for row in matrix]
```

### Core pattern

```text
[expression for item in iterable if condition]
     ↓             ↓             ↓
  what to store  where from   whether to keep
```

**L15 complete. ✅**
