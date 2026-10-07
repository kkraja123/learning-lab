# Traps

## Trap 1: finally can override return

- A return inside finally overrides the return from try.

def test():
    try:
        return 10
    finally:
        return 20

print(test()) => 20

## Trap 2 — finally and exceptions

- finally executes after the try/except processing and before execution continues beyond the entire construct.

try:
    print("A")
    raise ValueError("Error")
except ValueError:
    print("B")
finally:
    print("C")

print("D") => A B C D

## Trap 3 — else vs finally

| Block | When does it execute? |
|---|---|
| `try` | Always attempts the risky code |
| `except` | Only when a matching exception occurs |
| `else` | Only when `try` succeeds |
| `finally` | Normally always executes |

try:
    print("A")
except ValueError:
    print("B")
else:
    print("C")
finally:
    print("D") => A C D

## Trap 4 — raise without an except

- Create/raise a ValueError exception and begin exception handling/propagation.

def test():
    raise ValueError("Oops")
    print("After")

test() => terminates

## Trap 5

- the exception is raised again and propagates upward.
- Re-raise the exception that was just caught.

try:
    raise ValueError("A")
except Exception:
    print("B")
    raise

Interview rules to remember
1. Specific exceptions before general exceptions
2. else → runs only when try succeeds
3. finally → normally always runs
4. raise → explicitly raises an exception
5. Bare raise inside except → re-raises the current exception
6. Unhandled exceptions → propagate up the call stack
7. Avoid blindly doing except Exception: pass