# Truthiness

- Objects that represent "nothing" or "emptiness" are treated as False. Objects that represent "something" are treated as True.

| Object                 | Represents           | Truthiness |
| ---------------------- | -------------------- | ---------- |
| `0`                    | No quantity          | False      |
| `""`                   | No characters        | False      |
| `[]`                   | No elements          | False      |
| `{}`                   | No key-value pairs   | False      |
| Non-zero numbers       | Some quantity        | True       |
| Non-empty strings      | Some characters      | True       |
| Non-empty lists        | Some elements        | True       |
| Non-empty dictionaries | Some key-value pairs | True       |



if obj:
      │
      ▼
1. Does obj have __bool__()?
      │
      ├── Yes → Use its return value.
      │
      └── No
            │
            ▼
2. Does obj have __len__()?
      │
      ├── Yes
      │      len == 0 → False
      │      len > 0  → True
      │
      └── No
            │
            ▼
3. Default → True