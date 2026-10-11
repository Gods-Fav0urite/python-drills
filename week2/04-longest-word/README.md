# Longest Word

## Problem
Given a sentence, return the longest word. If two words tie, return the first one encountered.

## Function Signature
`longest_word(sentence) -> str`

## Examples
| input | output | why |
|---|---|---|
| `"the quick brown fox"` | `"quick"` | 5 chars, longest |
| `"hi there"` | `"there"` | tie goes to first (`"there"` is longer than `"hi"`, not a tie) |
| `"cat bat rat"` | `"cat"` | all 3 chars — first encountered wins |
| `"hello, world"` | `"hello"` | punctuation stripped before measuring |
| `""` | `""` | empty input, empty output |

## Assumptions
- split on whitespace to get tokens
- strip leading and trailing punctuation from each token before measuring (`"hello,"` → `"hello"`)
- ties go to the **first** word encountered
- empty string → return `""`
- a token that becomes empty after stripping (e.g. `"---"`) is ignored

## Hint
How would you remove punctuation characters from the start and end of a string without importing anything?

## Bonus
- handle multiple spaces between words
- return all words tied for longest as a list instead of just the first
