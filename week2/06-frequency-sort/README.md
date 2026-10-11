# Frequency Sort

## Problem
Given a list of numbers, sort it so the most frequent elements come first. If two elements have the same frequency, the smaller value comes first.

## Function Signature
`frequency_sort(items) -> list`

## Examples
| input | output | why |
|---|---|---|
| `[4, 5, 6, 5, 4, 4]` | `[4, 4, 4, 5, 5, 6]` | 4 appears 3×, 5 appears 2×, 6 appears 1× |
| `[1, 2, 2, 1, 3]` | `[1, 1, 2, 2, 3]` | 1 and 2 both appear 2×; 1 < 2 so 1 comes first |
| `[5]` | `[5]` | single element |
| `[]` | `[]` | empty list |

## Frequency Table for First Example
| value | frequency |
|---|---|
| 4 | 3 |
| 5 | 2 |
| 6 | 1 |

## Assumptions
- sort by **descending** frequency (highest count first)
- ties in frequency → **ascending** value (smaller number first)
- keep all duplicates — this is not deduplication
- return a **new list**, do not mutate the input

## Hint
Once you have each element's frequency, what two-value key would let you sort by frequency descending and value ascending at the same time?

## Bonus
- make it work for a list of strings, not just numbers
- handle the case where all elements are unique (every frequency is 1)
