# Variables

a = 10

- We are not storing 10 inside a.
- We are binding the name a to an object.

- Python doesn't really have "variables" in the C or Java sense.
- It has names.
- A name points to an object.

***Assignment changes bindings, not objects.***

| Code | New Object Created? | Existing Object Modified? |
|------|----------------------|---------------------------|
| `b.append(30)` | ❌ No | ✅ Yes |
| `b = b + [30]` | ✅ Yes | ❌ No |
| `b += [30]` | ❌ No *(for lists)* | ✅ Yes |

# is vs ==

- is will check the objects are same
- == will checck the values are same

# Mutable
- While doing the assignment(=), it will creates a new object
- While doing the slice, it will bind the same object
- The value cannot be changed, so that while slicing, python will not creating a new object.

# Mutable
- While doing the assignment(=), it will bind the same object
- While doing the slice, it will creates a new object
- The value can be changed, so that while slicing, Python will creating a new object.

# Mutable vs Immutable:

- A mutable object can change its internal state without changing which object a variable refers to.
- Immutable objects can't, so any apparent modification creates a new object and rebinds the name.

## Object Interning(Cache):

- Instead of creating identical immutable objects repeatedly, Python reuses an existing object.

# Goal:

- Save memory
- Reduce object creation
- Speed up comparisons

# Integer Interning:

- -5 to 256 will be in cache
- Based on python implementation and optimization "is" will differ

# String Interning:

- Strings are immutable.
- Python may reuse identical immutable string objects.
- The purpose is to save memory and improve performance.
- == compares values.
- is compares identity.

# copy (Shallow copy):

- Creates new object for outer list
- Shares the inner list

# Deep Copy:

- Creates new object for outer list and copy all the inner list

| Feature                       | Assignment (`=`) | Shallow Copy (`list.copy()`, `copy.copy()`) | Deep Copy (`copy.deepcopy()`) |
| ----------------------------- | ---------------- | ------------------------------------------- | ----------------------------- |
| Creates a new outer object?   | ❌ No             | ✅ Yes                                       | ✅ Yes                         |
| Copies nested objects?        | ❌ No             | ❌ No                                        | ✅ Yes                         |
| Shares inner mutable objects? | ✅ Yes            | ✅ Yes                                       | ❌ No                          |
| Independent outer list?       | ❌ No             | ✅ Yes                                       | ✅ Yes                         |
| Independent nested lists?     | ❌ No             | ❌ No                                        | ✅ Yes                         |
| Memory usage                  | Lowest           | Medium                                      | Highest                       |
| Speed                         | Fastest          | Fast                                        | Slowest                       |




