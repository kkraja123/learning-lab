# Return

- def → Creates only the Function Object.
- () → Executes the function body.
- return → Returns a reference to an object.
- = → Binds the returned reference to a variable.

* return sends an object reference back to the caller. The caller can bind that reference to a variable.

| `print()`                                 | `return`                                     |
| ----------------------------------------- | -------------------------------------------- |
| Displays something on the screen          | Sends an object reference back to the caller |
| Does not decide what the function returns | Decides what the function returns            |
| Side effect                               | Function result                              |


- print() is for humans. return is for the program.
- print() helps you see something.
- return helps another piece of code use something.
- When Python executes a return statement, the function ends immediately.

*** Every function returns something. ***

- If no return is written, Python returns None.
- print() and return have different purposes.
- return sends an object reference back to the caller.
- return immediately stops function execution.
- Code after an executed return is unreachable.
