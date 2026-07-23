# float

- A float object stores an approximation of many decimal numbers, not the exact decimal value.

- We almost never compare floats using ==.
- math.isclose(0.1 + 0.2, 0.3)

float
│
├── Stores binary numbers
├── Many decimal fractions cannot be stored exactly
├── Python stores the closest approximation
├── Arithmetic is performed on those approximations
└── Avoid == when comparing results of float calculations