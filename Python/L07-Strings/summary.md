# Summary:


📘 Lesson 7 — Strings: Complete Summary
You completed Lesson 7. The main goal was not just learning string methods, but understanding how strings behave as immutable Python objects and how to reason about their complexity.

1. String Object & Immutability
x = "Python"

Python creates a string object and binds x to it.
Strings are immutable.
So:
x[0] = "J"

❌ Not allowed.
You cannot modify the existing string object.
Instead:
x = "Python"
x = "Jython"

creates/binds to another string object.
Mental model
x ─────► "Python"

After reassignment:
x ─────► "Jython"

The original "Python" wasn't modified.

2. Multiple Names Can Reference One String
x = "Python"
y = x

Both names point to the same object:
       ┌──────────┐
x ─────►│ "Python" │
y ─────►│          │
        └──────────┘

Because strings are immutable, sharing the object is safe.

3. Indexing
x = "Python"

P  y  t  h  o  n
 0  1  2  3  4  5

Negative indexing:
-6 -5 -4 -3 -2 -1
 P  y  t  h  o  n


4. Slicing
The fundamental rule:
s[start:stop:step]

Start included, stop excluded.
Example:
x = "Python"
x[1:4]

Result:
yth

Default values
x[:]

means effectively:
start → beginning
stop  → end
step  → 1

For negative step:
x[::-1]

means reverse the string.
Important:
[::-2]

uses a negative step and Python determines the appropriate starting boundary automatically. Don't mentally force it into [-1:0:-2] unless you have explicitly established those bounds.

5. String Transformation Methods
These do not modify the original string.
They produce a resulting string.
upper()
lower()
capitalize()
replace()
strip()
lstrip()
rstrip()

Example:
x = "Python"
y = x.upper()

Conceptually:
x ──► "Python"

y ──► "PYTHON"


6. replace()
"banana".replace("a", "o")

Result:
bonono

By default, matching occurrences are replaced.
Important:
replace() creates a new string because strings are immutable.

7. find() vs index()
"banana".find("ana")

→ 1
If not found:
"banana".find("xyz")

→ -1
But:
"banana".index("xyz")

raises:
ValueError

Remember
find()  → not found → -1
index() → not found → exception


8. count()
"banana".count("a")

→ 3
It counts occurrences.
Important edge case:
"Python".count("")

→ 7
For a string of length n, the empty string can occur at n + 1 boundaries.

9. split()
x = "Python is powerful"
x.split()

Result:
["Python", "is", "powerful"]

Without an argument, split() uses whitespace.
It handles consecutive whitespace specially:
"  Python   is   powerful  ".split()

→
["Python", "is", "powerful"]

Important
It is not:
split("")

An empty string cannot be used as the separator.

10. join()
The direction is important:
String separator + iterable of strings
                ↓
              String

Example:
"-".join(["Python", "is", "powerful"])

→
Python-is-powerful

Very important DSA rule
For building a string from many pieces:
"".join(words)

is generally preferred over repeatedly doing:
result += word

because strings are immutable.

11. String Concatenation Performance
This:
result = ""

for word in words:
    result += word

can lead to repeated string creation/copying.
General interview-level complexity:
Repeated concatenation → O(n²)
join()                  → O(n)

The underlying reason:
String immutability.

12. strip()
This was one of your major learning points.
"   Python   ".strip()

→
Python

It removes whitespace only from the edges.
It does not remove spaces from the middle.

strip(chars) is NOT substring removal
"***abPythonba***".strip("*ab")

means:
Remove any *, a, or b characters from the edges.
It does not mean:
Remove the substring "*ab".

13. lstrip() / rstrip()
lstrip() → left
rstrip() → right
strip()  → both


14. startswith() / endswith()
"Programming".startswith("Pro")

→ True
"Programming".endswith("ming")

→ True
They return:
bool

They don't create a new string.
Start/end parameters
"Programming".startswith("gram", 3)

→ True
Because index 3 is g.
You also learned:
startswith(prefix, start, end)

with the normal slicing boundary rule:
start included, end excluded.
Empty string
"Python".startswith("")

→ True
"Python".endswith("")

→ True

15. Character Checking Methods
You learned an important general pattern:
These methods inspect characters and return a Boolean.
Usually:
Time  → O(n)
Space → O(1)


isalpha()
Every character must be alphabetic, and the string cannot be empty.
"Python".isalpha()     # True
"Python3".isalpha()    # False
"Python 3".isalpha()   # False
"".isalpha()           # False

Unicode letters are supported:
"தமிழ்".isalpha()      # True


16. isdigit()
Checks whether every character is a digit.
"123".isdigit()        # True
"12a".isdigit()        # False
"-123".isdigit()       # False
"12.5".isdigit()       # False
"".isdigit()           # False

Important:
isdigit() does not ask whether the whole string represents an integer.
It examines individual characters.

17. isdecimal() / isdigit() / isnumeric()
The hierarchy:
isdecimal()
     ↓
isdigit()
     ↓
isnumeric()

Think:
decimal digits
     ⬇
digits
     ⬇
numeric characters

Examples:
Character
Decimal
Digit
Numeric
3
✅
✅
✅
٣
✅
✅
✅
²
❌
✅
✅
½
❌
❌
✅
The key idea:
These methods inspect characters, not mathematical numbers.
Therefore:
"12.5".isnumeric()

→ False
because . isn't numeric.

18. isalnum()
You correctly decoded the name:
is + al + num

It means:
Every character must be alphabetic OR numeric.
Not AND.
Therefore:
"Python".isalnum()       # True
"123".isalnum()          # True
"Python123".isalnum()    # True
"Python_123".isalnum()   # False
"Python 123".isalnum()   # False
"".isalnum()             # False


19. islower()
Important subtle rule:
There must be at least one cased character, and all cased characters must be lowercase.
Characters without case—digits, spaces, punctuation—are ignored.
"python".islower()       # True
"python123".islower()    # True
"123python".islower()    # True
"Python".islower()       # False
"123".islower()          # False


20. isupper()
Mirror of islower():
There must be at least one cased character, and all cased characters must be uppercase.
"PYTHON".isupper()       # True
"PYTHON123".isupper()    # True
"123PYTHON".isupper()    # True
"PyTHON".isupper()       # False
"123".isupper()          # False


21. isspace()
This one you initially misunderstood, but you've got it now.
Rule:
The string must be non-empty and every character must be whitespace.
Whitespace includes:
space
tab
newline

Examples:
"   ".isspace()       # True
" \t\n".isspace()     # True
"a b".isspace()       # False
" 1 ".isspace()       # False
"".isspace()          # False

The key distinction:
"Does it contain a space?"
            ❌

"Are ALL characters whitespace?"
            ✅


22. == vs is
This was another major concept.
==
Checks value equality:
x == y

Do these objects have equal values?
is
Checks object identity:
x is y

Are these names bound to the exact same object?

23. String Interning
Python can reuse certain string objects.
x = "Python"
y = "Python"

Both may reference the same object:
      "Python"
       Object A
       ▲      ▲
       │      │
       x      y

Therefore x is y can be True.
But never rely on this for string comparison.
Always use:
x == y

when you mean:
"Do these strings have the same value?"

24. join() and Object Identity
You tested:
x = "Python"
y = "".join(["Py", "thon"])

You correctly concluded:
x == y     # True
x is y     # False

The important lesson:
Same value ≠ necessarily same object


🧠 Your Lesson 7 DSA Cheat Sheet
If you remember only this:
STRING
│
├── Immutable
│
├── Index/Slice
│   └── [start:stop:step]
│
├── Search
│   ├── find()   → -1 if missing
│   ├── index()  → ValueError if missing
│   └── count()
│
├── Transform
│   ├── upper()
│   ├── lower()
│   ├── replace()
│   └── strip()
│
├── Split/Build
│   ├── split()  → list
│   └── join()   → string
│
├── Check
│   ├── startswith()
│   ├── endswith()
│   ├── isalpha()
│   ├── isdigit()
│   ├── isalnum()
│   ├── islower()
│   ├── isupper()
│   └── isspace()
│
└── Identity
    ├── == → value
    └── is → object

Most important DSA concepts from Lesson 7
1. Immutable → transformations create new strings
2. join() → efficient string construction
3. split() ↔ join()
4. find() → -1, index() → exception
5. strip() → edges only
6. isalnum() → alphabet OR digit
7. islower() / isupper() → uncased characters are ignored
8. == → value, is → identity
9. Most character-checking methods → O(n) time, O(1) auxiliary space
10. String interning is an optimization, not something to rely on.
