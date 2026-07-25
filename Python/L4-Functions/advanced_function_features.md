# Advanced Function Features

- Multiple return values
- Returning multiple objects
- Early returns
- Nested function calls
- Function call stack (visualized with memory diagrams)
- Why return a, b works even though a function returns only one object

* A function returns exactly one object reference.
* That object is a Tuple Object.

## Tuple Unpacking

Python conceptually does this:

### return 10, 20

- Create (or evaluate) the Integer Object 10.
- Create (or evaluate) the Integer Object 20.
- Create a Tuple Object.
- Store references to 10 and 20 inside the tuple.
- Return one reference — the reference to the Tuple Object. 

*** The number of variables on the left must exactly equal the number of items in the iterable being unpacked.***

## Early Return:

- When Python executes a return statement, the current function immediately stops executing.

## Function Stack:

*** Last In → First Out (LIFO) ***

## The Golden Rule

* A function call does two things:

- Creates a new function frame.
- Pushes that frame onto the call stack.

* When the function returns:

- The frame is destroyed.
- It is popped from the top of the stack.
