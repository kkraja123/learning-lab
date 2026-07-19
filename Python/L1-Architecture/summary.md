# Lesson 1 Summary - Python Architecture

## Python execution flow

- Source Code (.py) -> Python Parser -> Abstract Syntax Tree (AST) -> Python Compiler -> Bytecode (.pyc) -> Python Virtual Machine (PVM) -> Operating System -> CPU executes

## CPython

- Python is a language specification.
- CPython is the reference implementation.
- Why CPython is written in C.

## Other implementations:

1. CPython
2. PyPy
3. Jython
4. IronPython
5. MicroPython

## Bytecode

- Why Python compiles to bytecode.
- Why bytecode improves portability.
- Bytecode is executed by the PVM.

## __pycache__
- Why .pyc files are created.
- Why imported modules are cached.
- Cache validation using source metadata.
- When recompilation occurs.

## Import System

- sys.modules
- Module caching
- Search order (simplified and then refined)
- Current project vs standard library vs third-party packages
- Module shadowing
- Why requests.py or json.py are bad filenames

## Module Objects

This is the biggest concept from Lesson 1.

- A module is an object.
- Python executes a module only once.
- Every import returns the same module object.
- Modules behave like singletons within one Python process.
- importlib.reload() re-executes a module.

## Namespace vs Module

Difference between: import math and from math import sqrt

- Imported names are ordinary names in your namespace.
- They can be rebound.
- Rebinding doesn't modify the original module.

## What You Can Now Explain

If an interviewer asks any of these:

- "How does Python execute code?"
- "What is bytecode?"
- "What is CPython?"
- "What is the PVM?"
- "What is __pycache__?"
- "How does Python decide whether to compile?"
- "What is sys.modules?"
- "Why is importing the same module twice fast?"
- "Why shouldn't I name my file json.py?"
- "Difference between import x and from x import y?"