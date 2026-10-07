# Modules And Packages

L20 sequence
1. What is a module?
2. import
3. from ... import
4. Module namespace
5. __name__
6. if __name__ == "__main__"
7. Import execution behavior
8. Packages
9. __init__.py
10. Absolute vs relative imports
11. Common import problems
12. Interview traps

## Module

- A module is essentially a Python file (.py) that contains Python code—functions, classes, variables, etc.—which can be imported and reused.

calculator.py
     ↓
   module
     ↓
import calculator
     ↓
calculator namespace
     ↓
calculator.add(...)

## from ... import

- from calculator import add imports the add name directly into the current module's namespace

- import module → bring the module name
- from module import name → bring a specific name

from calculator import add
add(10, 20)

## Module Namespace

- each module has its own namespace.

main namespace
└── x → 500

calculator namespace
└── x → 100

## __name__

- To define the class name(kind of)

## if __name__ == "__main__"

- Run this block only when this file is executed directly.

This pattern lets a file work as both:
- a reusable module
- a directly executable script

| How file is used | `__name__` |
|---|---|
| Run directly | `"__main__"` |
| Imported | module name, e.g. `"calculator"` |

## Import execution behavior

import calculator
      ↓
Find/load module
      ↓
Execute top-level code
      ↓
Store module in sys.modules

## Packages

- A package is used to organize related modules into a structured namespace.

| | Module | Package |
|---|---|---|
| Usually | `.py` file | Directory/folder |
| Contains | Functions, classes, variables | Modules/subpackages |
| Example | `upi.py` | `payments/` |
| Purpose | Organize code | Organize modules |

## Absolute vs Relative Imports

Absolute - from payments import upi
Relative - from . import upi

