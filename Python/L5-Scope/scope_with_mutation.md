# Scope with Mutation

x = [10]

def show():
    x.append(20)

show()
print(x)

- No assignment.
- No local variable.

## Mutates global object.

x = [10]

def show():
    x = [20]

- Assignment.
- Creates local variable.
- Global list untouched.