# Space Complexity:

- "How much does the memory grow?"


I want you to memorize this thought process, not the answers.

Whenever you see an algorithm, ask yourself:

Am I creating a new data structure?
Yes → It might be O(n) or more.
No → Continue.
Am I only using a few variables?
Yes → O(1)
Does the extra memory grow as n grows?
Yes → Not O(1)
No → O(1)


"Is a new data structure created?"
"Does memory grow?"
"How many elements are stored?"

Changing the value of a variable does not increase Space Complexity. Creating additional memory that grows with the input does.