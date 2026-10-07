# Exceptions

## What we'll cover
1. What is an exception?
2. Errors vs exceptions
3. try / except
4. Catching specific exceptions
5. Multiple except blocks
6. else
7. finally
8. raise
9. Custom exceptions
10. Exception propagation
11. Exception hierarchy
12. Common interview traps

## Exception

- An exception is an object representing an abnormal situation that occurs while the program is running.

## Try / Expect

- Try this operation. If a particular exception happens, handle it here.
- Execute this code. If an exception occurs, check whether one of the following except handlers can handle it.
- An except block handles an exception only if its specified exception type matches the raised exception (including through inheritance).

try
 ↓
Run risky code
 ↓
Exception?
 ├── No → continue normally
 └── Yes → find matching except

 ## Multiple Expect

 - Only one matching except block executes.

 ## Else

 - else executes only when the try block completes without an exception.

 | Situation | `except` | `else` |
|---|---|---|
| Exception occurs | ✅ | ❌ |
| No exception | ❌ | ✅ |

- else means: "The risky operation succeeded, so do the success-path work.
- else is useful when you want to keep success-only code outside the try block.

## Finally

- It normally executes whether the try succeeds or an exception occurs.

try
 ↓
 ├── success ──→ else
 │
 └── exception → except
        ↓
     finally

try:
    # risky operation

except SomeError:
    # handle exception

else:
    # runs when no exception

finally:
    # cleanup

# Raise

- This situation is invalid. Stop normal execution and signal an exception.
- raise doesn't just print an error. It actually raises an exception object.
- Once executes, The remaining statements in the current execution path are skipped.

# Custom Exceptions

- A custom exception gives your application a specific meaning and allows callers to handle that condition separately.

# Exception Propagation

- Exception propagation is the process by which an unhandled exception moves up the call stack until a matching except handler is found.

# Exception Hierarchy

BaseException
    └── Exception
         └── ArithmeticError
              └── ZeroDivisionError

BaseException
└── Exception
    ├── ArithmeticError
    │   └── ZeroDivisionError
    ├── ValueError
    ├── TypeError
    └── ...

More specific → first
More general → later