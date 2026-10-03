# OOP

Classes
Objects
__init__
Instance attributes
Class attributes
Methods
Inheritance
Polymorphism
Encapsulation
Composition

| OOP concept             | Your food-delivery example                     |
| ----------------------- | ---------------------------------------------- |
| **Class**               | `Order`, `Customer`, `Payment`                 |
| **Object**              | `order1`, `order2`                             |
| **`__init__`**          | Initializes order state                        |
| **Instance attributes** | `self.order_id`, `self.total_amt`              |
| **Class attributes**    | Shared values such as platform fee             |
| **Methods**             | `confirm()`, `pay()`                           |
| **`self`**              | Current `Order`/`Payment` object               |
| **Inheritance**         | `UPIPayment` → `Payment`                       |
| **Polymorphism**        | `payment.pay()` behaves differently            |
| **Encapsulation**       | Controlled modification of `_total_amt`        |
| **Composition**         | `Order` HAS-A `Payment`, `Customer`, `Address` |


**🧠 The one story to remember

Imagine you're explaining the system in an interview:

"We model an Order as a class. Each order is an object with its own state such as order ID and total amount, initialized through __init__. Methods such as confirm() define the order's behavior. Payment types can inherit from a common Payment class and override pay(), giving us polymorphism. Internal order state can be protected through encapsulation, and Order can contain Payment and Customer objects through composition."

That's a real OOP explanation, not a collection of definitions. 💯 **


What you got right ✅
- Class → defines the structure/behavior of objects.
- Customer, Order, Payment, Product → reasonable classes for the system.
- Inheritance → parent/child relationship.
- Encapsulation → controlling access/modification of internal state.
- Composition → relationships where one object contains/uses another.

** OOP in Python is a way of structuring software using objects that combine state and behavior.

In a food-delivery system, we might have classes such as Customer, Order, Payment, and Product. Each object created from these classes has its own state and behavior.

Inheritance allows specialized classes such as UPIPayment and CardPayment to derive from a common Payment class.

Polymorphism allows us to call the same interface, such as payment.pay(), while different payment objects provide different implementations.

Encapsulation means keeping an object's internal state controlled through its defined interface.

Composition represents HAS-A relationships. For example, an Order can contain a Payment, Customer, and delivery Address.

So, OOP helps us model real-world entities by combining their state, behavior, and relationships.**

Class       → What can exist?
Object      → One actual instance
Inheritance → IS-A
Polymorphism→ Same interface, different behavior
Encapsulation→ Control internal state
Composition → HAS-A
