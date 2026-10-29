# Advanced Iteration

## Generators: lazy execution

- A generator can produce values one at a time instead of creating all the values at once. But the most important detail is when its code executes.

def generate_numbers():
    print("Start")
    yield 10
    print("Middle")
    yield 20
    print("End")

g = generate_numbers()
print("Created")

print(next(g))

1. When generate_numbers() is called and g is created.
2. When next(g) requests the first value.

**Calling a generator function**
- Creates a generator object without executing the function body.

**Calling next(g)**
- Starts or resumes execution until the next yield or until the generator terminates.

- yield suspends execution; the next next() resumes it. 
- StopIteration occurs only when the generator finishes.

**Key concept:** 
- generators are one-shot iterators. 
- Creating a new list from a generator **doesn't reset** it.
- To generate the values again, create a new generator object

## yield versus return

| Statement | Generator behavior |
|---|---|
| `yield 10` | Produces 10 and suspends execution |
| `return` | Ends the generator with no explicit return value |
| `return 99` | Ends the generator; `StopIteration.value` is 99 |

def example():
    yield "A"
    return "Done"

g = example()

print(list(g))

1. yield "A" produces the only yielded item.
2. return "Done" terminates the generator.
3. Python signals termination through StopIteration, whose .value is "Done".
4. list(g) handles that termination automatically and collects only yielded values.
So "Done" is a return value, not a yielded item.

## Generator state: what does send() do?

def receiver():
    value = yield 10
    yield value

g = receiver()

print(next(g))
print(g.send(50))

1. next(g)
- Starts executing receiver().
- Reaches yield 10.
- Produces 10 and suspends the generator.
2. g.send(50)
- Resumes the suspended generator.
- The expression yield 10 evaluates to 50.
- Assigns 50 to value.
- Reaches yield value, producing 50.
The key distinction:
- yield 10 sends 10 out to the caller.
- g.send(50) sends 50 into the suspended generator.
A generator must be started before you send it a non-None value; otherwise, Python raises TypeError.

## What happens when you send too early?

- TypeError: can't send non-None value to a just-started generator

## yield from: delegation

def child():
    yield 1
    yield 2

def parent():
    yield 0
    yield from child()
    yield 3

print(list(parent())) ==> [0, 1, 2, 3]

1. yield 0 produces 0.
2. yield from child() delegates iteration to child(), producing 1, then 2.
3. When child() finishes, parent() resumes after yield from.
4. yield 3 produces 3.

**The key difference**
- yield child() yields the generator object itself as one value.
- yield from child() delegates to the generator and yields its values individually.
yield from is useful for composing generators without manually writing a loop to forward every value.

## What does close() do?

- close() is useful for terminating a generator and triggering cleanup, such as releasing resources. It does not resume normal iteration to produce all remaining values.

### What if the generator yields after close()?

- After close(), the generator is permanently exhausted. Calling next(g) raises StopIteration

## Injecting exceptions with throw()

def numbers():
    try:
        yield 1
    except ValueError:
        yield 99

g = numbers()

print(next(g)) 1
print(g.throw(ValueError)) 99

First call — next(g)
- Starts the generator.
- Reaches yield 1.
- Prints 1 and suspends.
Second call — g.throw(ValueError)
- Injects a ValueError at the generator's suspension point.
- The except ValueError handler catches it.
- The handler executes yield 99.
- The call returns 99, which the outer print() displays.