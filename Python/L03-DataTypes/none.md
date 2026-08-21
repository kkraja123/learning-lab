# None

- What None really is.
- Why None is not 0, False, or "".
- Why we write is None instead of == None.
- Why functions return None by default.
- Common interview questions about None.
- Common bugs caused by comparing None incorrectly.



== can be customized by a class.

is cannot be customized.

✅ None is a singleton object.
✅ Its type is NoneType.
✅ Every function returns an object; if there's no explicit return, Python returns None.
✅ Use is None, not == None.
✅ is checks object identity; == checks value equality.
✅ == can be customized via __eq__; is cannot.
✅ Many in-place methods return None intentionally to indicate they modified the existing object.