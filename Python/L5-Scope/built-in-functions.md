# Object Model:


| Expression               | Kind of Object           | Created By      | `type(...)`                  | Calling `()` Does What?         |
| ------------------------ | ------------------------ | --------------- | ---------------------------- | ------------------------------- |
| `10`                     | Integer instance         | Python          | `int`                        | ❌ Not callable                  |
| `"hello"`                | String instance          | Python          | `str`                        | ❌ Not callable                  |
| `[]`                     | List instance            | Python          | `list`                       | ❌ Not callable                  |
| `{}`                     | Dictionary instance      | Python          | `dict`                       | ❌ Not callable                  |
| `Student`                | Class object             | `type`          | `type`                       | ✅ Creates a `Student` instance  |
| `list`                   | Class object             | `type`          | `type`                       | ✅ Creates a list instance       |
| `dict`                   | Class object             | `type`          | `type`                       | ✅ Creates a dictionary instance |
| `int`                    | Class object             | `type`          | `type`                       | ✅ Creates an integer instance   |
| `type`                   | Class object             | Itself*         | `type`                       | ✅ Creates a class object        |
| `print`                  | Built-in function object | Python          | `builtin_function_or_method` | ✅ Executes the function         |
| `len`                    | Built-in function object | Python          | `builtin_function_or_method` | ✅ Executes the function         |
| `greet` *(user-defined)* | Function object          | Python          | `function`                   | ✅ Executes the function         |
| `Student()`              | Student instance         | `Student` class | `Student`                    | Depends on the instance         |
| `list()`                 | List instance            | `list` class    | `list`                       | Depends on the instance         |

| Object    | `type(...)`                  |
| --------- | ---------------------------- |
| `10`      | `int`                        |
| `"abc"`   | `str`                        |
| `[]`      | `list`                       |
| `Student` | `type`                       |
| `list`    | `type`                       |
| `print`   | `builtin_function_or_method` |
| `greet`   | `function`                   |


# Callable objects:

| Object    | Callable? | Result of `()`             |
| --------- | --------- | -------------------------- |
| `print`   | ✅         | Executes the function      |
| `len`     | ✅         | Executes the function      |
| `list`    | ✅         | Creates a list instance    |
| `Student` | ✅         | Creates a Student instance |
| `10`      | ❌         | TypeError                  |
| `"hello"` | ❌         | TypeError                  |
| `[]`      | ❌         | TypeError                  |
