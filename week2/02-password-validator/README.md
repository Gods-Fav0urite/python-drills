# Password Validator

## Problem
Check whether a password meets all five security rules. Return `True` if all pass, `False` if any fail.

## Function Signatures (core)
`has_min_length(password) -> bool`
`has_uppercase(password) -> bool`
`has_lowercase(password) -> bool`
`has_digit(password) -> bool`
`has_special(password) -> bool`
`is_valid_password(password) -> bool`


## Examples
| input | output | why |
|---|---|---|
| `is_valid_password("Hello@12")` | `True` | all 5 rules pass |
| `is_valid_password("hello@12")` | `False` | no uppercase letter |
| `is_valid_password("Hi@1")` | `False` | fewer than 8 characters |
| `has_special("Hello World")` | `False` | space does not count as special |

## Requirements
Implement all five `has_*` functions, then implement `is_valid_password` by calling them — don't repeat the logic inside `is_valid_password`.

Rules:
- minimum 8 characters
- at least one uppercase letter (A–Z)
- at least one lowercase letter (a–z)
- at least one digit (0–9)
- at least one special character

## Assumptions
- special character = any character that is not a letter, digit, or whitespace (`!@#$%^&*` etc.)
- a space is **not** a special character
- functions return `bool` — do not print
- `is_valid_password` uses the five helper functions; don't duplicate the checks

## Hint
How would you check if *at least one* character in a string satisfies a condition, without writing a manual `for` loop with a flag variable?

## Bonus
Implement `get_failed_requirements(password) -> list[str]`

Returns a list of the rule names that failed, in this order:
`"min_length"`, `"uppercase"`, `"lowercase"`, `"digit"`, `"special"`

Returns `[]` if the password is valid.

```python
get_failed_requirements("hello@12")  # → ["uppercase"]
get_failed_requirements("")          # → ["min_length", "uppercase", "lowercase", "digit", "special"]
```