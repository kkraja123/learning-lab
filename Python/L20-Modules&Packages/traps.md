# Traps

## Trap 1

project/
└── payments/
    ├── __init__.py
    ├── upi.py
    └── card.py

from . import upi

Relative import error occurs because card.py is being executed as a standalone script
we need to run as module

## Trap 2

project/
├── main.py
└── random.py

import random
print(random.randint(1, 10))

Your local random.py can shadow Python's standard-library random module

**A module is a Python file that provides a namespace for reusable code. A package organizes related modules into a namespace hierarchy. import loads and binds a module, while from ... import binds selected names. Python caches loaded modules in sys.modules, and __name__ == "__main__" identifies direct execution.**