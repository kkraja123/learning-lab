# Class

A class defines the common structure and behavior, while each object maintains its own state/values.

Order class
 ├── common structure
 └── common behavior
        ↓
   ┌──────────────┐
   │              │
order_101      order_102
   ↓              ↓
own state       own state


| Concept                | Meaning                           |
| ---------------------- | --------------------------------- |
| **Class**              | Blueprint/definition for objects  |
| **Object**             | Individual instance               |
| **`__init__`**         | Initializes instance state        |
| **Instance attribute** | Data belonging to one object      |
| **Class attribute**    | Data associated with the class    |
| **Method**             | Behavior defined inside the class |
| **`self`**             | The current object                |