# List

## Comprehension

[expression **for** item **in** iterable **if** condition]

[n * 10 for n in x if n > 2]
 ↑              ↑
expression      condition


| Operation     | Modifies original? | Returns  | Complexity      |
| ------------- | ------------------ | -------- | --------------- |
| `x.reverse()` | Yes                | `None`   | O(n)            |
| `reversed(x)` | No                 | Iterator | O(n) to consume |
| `x.sort()`    | Yes                | `None`   | O(n log n)      |
| `sorted(x)`   | No                 | New list | O(n log n)      |
