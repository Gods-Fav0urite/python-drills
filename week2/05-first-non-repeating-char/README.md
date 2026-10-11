# First Non-Repeating Character

## Problem
Given a string, return the first character that appears exactly once. If no such character exists, return `None`.

## Function Signature
`first_non_repeating(s) -> str | None`

## Examples
| input | output | why |
|---|---|---|
| `"aabbcde"` | `"c"` | `a` and `b` repeat; `c` is first with frequency 1 |
| `"aabb"` | `None` | every character repeats |
| `"z"` | `"z"` | only one character, appears once |
| `"aAbBc"` | `"a"` | `'a'` and `'A'` are different characters; `'a'` appears once |
| `""` | `None` | empty string |

## Assumptions
- case-sensitive: `'A'` and `'a'` are treated as different characters
- return the first non-repeating character by **position in the original string**, not alphabetically
- return `None` (not `""`, not `"None"`) when none exists

## Hint
What data structure lets you count how many times each character appears in one pass?

## Bonus
- make it case-insensitive (add a `case_sensitive=True` parameter)
- count only alphabetic characters, ignoring digits and spaces
