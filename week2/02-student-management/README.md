# Student Management System

## Problem
Store student records as a list of dictionaries and add, find, update, remove and rank them.

```python
students = [
    {"id": 1, "name": "Ada", "scores": [80, 75, 90]},
    {"id": 2, "name": "Tunde", "scores": [60, 85, 70]},
]
```

## Function Signatures
- `add_student(students, student) -> bool`
- `find_student(students, student_id) -> dict | None`
- `calculate_average(scores) -> number`
- `get_grade(average) -> str`
- `update_student_name(students, student_id, new_name) -> bool`
- `get_top_student(students) -> dict | None`
- `get_students_above_average(students, threshold) -> list[dict]`
- `remove_student(students, student_id) -> bool`

## Examples
| input | output | why |
|---|---|---|
| `add_student(students, {"id": 3, "name": "Bola", "scores": [50]})` | `True`, student appended | valid new student |
| `add_student(students, {"id": 1, "name": "Ada II", "scores": [10]})` | `False` | id 1 already exists, adding the same id twice is rejected |
| `find_student(students, 2)` | `{"id": 2, "name": "Tunde", ...}` | found by id |
| `find_student(students, 99)` | `None` | no such id |
| `calculate_average([80, 75, 90])` | `81.67` | 245 / 3, rounded to 2 decimals |
| `calculate_average([])` | `0` | no scores, no division by zero |
| `get_grade(70)` | `"A"` | lower bound of A is inclusive |
| `get_top_student(students)` | Ada's record | 81.67 beats 71.67 |
| `get_students_above_average(students, 75)` | `[Ada]` | only averages strictly above 75 |
| `remove_student(students, 2)` | `True`, only Tunde removed | removes exactly one record |

## Assumptions
- a student record needs an `id` (whole number), a non-empty `name`, and a `scores` list; each score is a number from 0 to 100 inclusive (`bool` and `nan` rejected)
- `add_student`, `update_student_name`, `remove_student` change `students` in place and return `True` (done) or `False` (rejected, nothing changed)
- `add_student` rejects: not a dict, bad or missing id, empty or whitespace-only name, missing or invalid scores, and an id that already exists (so adding the same student twice fails). an empty `scores` list is allowed
- the stored record is a copy: name is stripped and the scores list is copied, so changing the original afterwards does not touch the stored one
- `find_student` returns the record itself (not a copy), or `None`; a non-int id (`"1"`, `1.0`, `True`) finds nothing. if duplicate ids exist in a hand-built list, the first one wins
- `calculate_average` rounds to 2 decimals, returns `0` for an empty list, and raises `ValueError` for anything that is not a list of valid scores (including `None`)
- grading scale (inclusive lower bounds): A 70-100, B 60-69, C 50-59, D 45-49, E 40-44, F 0-39. `get_grade` raises `ValueError` for a non-number or a value outside 0 to 100. averages between whole numbers follow the lower bound (69.99 is B)
- `update_student_name` strips the name; unknown id or empty/whitespace/non-string name returns `False` and changes nothing
- `get_top_student` returns the record with the highest average, the first in the list on a tie, and `None` for an empty list. a student with no scores has average `0`
- `get_students_above_average` keeps list order and uses strictly greater than. `threshold` must be a number or it raises `ValueError`
- `get_top_student` and `get_students_above_average` raise `ValueError` if any record has missing or invalid scores, so bad data is never hidden
- `remove_student` removes the first record with that id and nothing else, and returns `False` if there is none

## Hint
what goes wrong if you call `students.remove(...)` inside a `for` loop over `students` and keep looping?