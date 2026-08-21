# String

- What exactly is a string object?
- Why are strings immutable?
- Memory model of strings.
- Unicode and UTF-8 (why Python 3 handles emojis and all languages correctly).
- Indexing.
- Negative indexing.
- Slicing (one of Python's most powerful features).
- Common string methods (split, join, replace, strip, find, etc.).
- Why += on strings creates new objects.
- String interning.
- Performance (+ vs join).
- Common interview questions.
- CPython implementation details (where useful).
- Real-world examples and exercises.


***"A string is an immutable sequence of Unicode characters represented by a str object."***

# Slicing
- Why is the end index excluded?
- Why does [::-1] reverse a string?
- What exactly does the second : mean?
- Does slicing create a new object?
- Why doesn't slicing throw an error when the end index is too large?
- What happens internally?

- Choose the start index.
- Choose the stop index.
- If either is outside the valid range, clamp it to the nearest valid boundary.
- Return everything from start (inclusive) to stop (exclusive).

Strings are str objects.
✅ Indexing returns a str object (length 1).
✅ Positive indexing.
✅ Negative indexing.
✅ Why -0 doesn't exist.
✅ Why IndexError exists.
✅ How Python conceptually converts negative indexes.
✅ The connection between indexing and the object model.

1. Stand on the start index. 
2. Look at the step. +ve → Walk right -ve → Walk left 
3. Can I reach the stop? No → "" Yes → Keep walking. 
4. Collect characters. 
5. Never collect the stop index.