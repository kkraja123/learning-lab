# Lesson 3 Summary

## String indexing

- Positive indexing
- Negative indexing
- IndexError

## String slicing

- start:stop
- Half-open interval (stop excluded)
- Positive and negative indices
- Positive and negative steps
- Step as direction + jump size
- Empty slices
- Default values (name[:], name[::2], etc.)

## Memory model

- Variables vs objects
- References
- id()
- Assignment
- Rebinding

## Mutability

- Mutable vs immutable objects
- Why strings behave differently from lists

## Copying

- List slicing creates a new outer list
- String slicing may reuse the same object (CPython optimization)
- Shallow copy
- Nested lists and shared inner objects

## Function preview

- Function parameters are local variables that refer to the passed object.
- Difference between modifying an object and rebinding a local variable.