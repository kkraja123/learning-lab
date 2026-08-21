Python is a ***language*** specification.
CPython is an ***implementation*** of that specification.

Python Language Specification
        │
        ├── CPython  ← Most popular
        ├── PyPy
        ├── Jython
        ├── IronPython
        └── MicroPython

## Why Does Python Have Multiple Implementations?

- Because Python defines what the language should do, not how it must be implemented.

# CPython:

- The reference implementation of Python written primarily in C.

## Why was it written in C?

- Excellent performance
- Direct memory access
- Easy integration with operating systems
- Mature compiler support
- Portability


| Implementation | Written In | Runs On | Best Use Case |
|----------------|------------|---------|---------------|
| CPython | C | Native OS | General-purpose Python, backend development, Machine Learning, scripting |
| PyPy | RPython | Native OS | Faster execution for long-running Python applications |
| Jython | Java | Java Virtual Machine (JVM) | Integration with Java applications and libraries |
| IronPython | C# | .NET Common Language Runtime (CLR) | Integration with the .NET ecosystem |
| MicroPython | C | Microcontrollers | Embedded systems, IoT devices, and microcontroller programming |

# Bytecode Cache (`.pyc`)

## Purpose
- Avoid recompiling imported Python modules.
- Improve import performance.

## Where is it stored?
- `__pycache__/module_name.cpython-313.pyc`

## When is `.pyc` created?
- Usually when a module is imported.
- The entry script (`main.py`) is typically not cached when executed directly.

## Cache Validation
Before using a cached `.pyc`, CPython checks:
- Source file modification time (mtime)
- Source file size

If either differs:
- Recompile source
- Generate new `.pyc`

Otherwise:
- Load bytecode directly from cache

## Flow

Import Module
↓
`.pyc` exists?
↓
Yes → Validate cache
↓
Valid → Execute `.pyc`
Invalid → Recompile → Update `.pyc`

## Notes
- `__pycache__` is safe to delete.
- Python recreates it automatically.
- Cache validation is timestamp-based by default.
- Hash-based validation is also supported (PEP 552).

# The Python Import System
1. Python Reads the Import Statement
2. Search Order
    import math -> Already imported? -> Built-in module? -> Current project? -> Python standard library? -> Installed packages (site-packages)? -> Module Not Found

