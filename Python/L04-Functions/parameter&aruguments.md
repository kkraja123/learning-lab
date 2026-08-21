# Parameter And Arguments

- Parameter = Variable inside the function.
- Argument = Actual value you pass while calling the function.

| Code                  | What changes?                  |
| --------------------- | ------------------------------ |
| `x = "Raja"`          | Reference changes              |
| `items.append(4)`     | Object changes                 |
| `items = items + [4]` | New object + reference changes |
| `x = x + "!"`         | New object + reference changes |


You've mastered:

- Parameters vs arguments
- Parameters are local variables
- Arguments are passed by reference (more precisely, object references are passed)
- Rebinding vs mutation
- Why append() behaves differently from +
- Memory model of function calls