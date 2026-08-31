Here’s the **short, crisp L17 cheat sheet** covering everything:

## L17 — Function Deep Dive 🧠

| Topic                        | Key idea                                                            |
| ---------------------------- | ------------------------------------------------------------------- |
| **Closures**                 | Inner function remembers variables from enclosing function          |
| **`nonlocal`**               | Modify a variable from the nearest enclosing function scope         |
| **Decorators**               | Add/modify function behavior without changing the original function |
| **`@decorator`**             | `func = decorator(func)`                                            |
| **Wrapper**                  | Inner function that surrounds/calls the original function           |
| **`*args` / `**kwargs`**     | Forward arbitrary positional/keyword arguments                      |
| **Return preservation**      | Wrapper must `return func(...)` if caller needs the result          |
| **Multiple decorators**      | `@A @B` → `func = A(B(func))`; execution is outer → inner           |
| **Parameterized decorators** | `@repeat(3)` needs 3 layers: configuration → decorator → wrapper    |
| **Function metadata**        | `__name__`, `__doc__`, etc.                                         |
| **`functools.wraps`**        | Copies important metadata from original function to wrapper         |
| **`functools.partial`**      | Creates a new callable with some arguments pre-filled               |
| **`functools.reduce`**       | Repeatedly combines values → one final result                       |
| **Accumulator**              | Result carried from one `reduce()` step to the next                 |
| **`lru_cache`**              | Caches results based on function arguments                          |
| **Cache limitation**         | Arguments must be hashable                                          |

### 🔑 Core mental models

```text
Closure
outer variable → remembered by inner
```

```text
Decorator
original function → wrapper → modified behavior
```

```text
partial()
function + fixed arguments → new callable
```

```text
reduce()
many values → repeated combination → ONE value
```

```text
lru_cache
arguments → cache → reuse previous result
```

**L17 = Functions as objects + functions modifying/wrapping other functions.**
