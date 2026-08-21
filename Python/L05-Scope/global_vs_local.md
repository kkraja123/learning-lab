# Global vs Local

*** Global frame ***

Step 1

- Look in the current function frame.
- If found → use it.
- If not...

Step 2

- Look in the Global Frame.
- If found → use it.
- If not...

Finallly:

- NameError


Python always searches from the innermost scope outward.


*** If Python has already decided a variable is local, it doesn't search the Global Frame for that variable. ***


1. How does Python know x is local before reaching x = 20?

- Because it analyzes the entire function body when creating the Function Object.

2. Why doesn't it simply use the global x?

- Because Python has already classified x as local for this function.
- Searching globally would violate that decision.

3. What is Python doing before the function even starts executing?

- It is creating the Function Object and recording information about the function, including which names are local variables.