import copy

from student_management import (
    add_student,
    find_student,
    calculate_average,
    get_grade,
    update_student_name,
    get_top_student,
    get_students_above_average,
    remove_student,
)

# contract: add/update/remove change the list in place and return True (done) or False (rejected,
# nothing changed). a student is {"id": int, "name": non-empty str, "scores": list of numbers 0..100}.
# grading: A 70+, B 60+, C 50+, D 45+, E 40+, F below 40 (lower bounds inclusive).
# average rounds to 2 decimals; empty scores -> 0. tie on top student -> first in the list.
# bad scores raise ValueError in calculate_average, get_top_student, get_students_above_average.

NAN = float("nan")
ADA = {"id": 1, "name": "Ada", "scores": [80, 75, 90]}      # average 81.67
TUNDE = {"id": 2, "name": "Tunde", "scores": [60, 85, 70]}  # average 71.67

failures = 0


def fresh():
    return [copy.deepcopy(ADA), copy.deepcopy(TUNDE)]


def fail(label, expected, got):
    global failures
    failures += 1
    print(f"FAIL: {label}")
    print(f"  expected: {expected}")
    print(f"  got:      {got}\n")


def is_num(x):
    return isinstance(x, (int, float)) and not isinstance(x, bool)


def check(label, call, expected, state=None, expected_state=None):
    try:
        got = call()
    except Exception as e:
        got = f"raised {type(e).__name__}: {e}"
    same_type = type(got) == type(expected) or (is_num(got) and is_num(expected))
    if got != expected or not same_type:
        fail(label, expected, got)
    elif state is not None and state != expected_state:
        fail(label + " (list after)", expected_state, state)


def check_raises(label, call):
    try:
        got = call()
    except ValueError:
        return
    except Exception as e:
        fail(label, "ValueError", f"raised {type(e).__name__}: {e}")
        return
    fail(label, "ValueError", f"returned {got!r}")


# ---------- add_student ----------
s = fresh()
bola = {"id": 3, "name": "Bola", "scores": [50, 60]}
check("add valid student", lambda: add_student(s, bola), True, s, fresh() + [bola])

s = fresh()
check("add strips the name", lambda: add_student(s, {"id": 3, "name": "  Bola  ", "scores": [50]}), True,
      s, fresh() + [{"id": 3, "name": "Bola", "scores": [50]}])

s = fresh()
check("add student with no scores", lambda: add_student(s, {"id": 3, "name": "Bola", "scores": []}), True,
      s, fresh() + [{"id": 3, "name": "Bola", "scores": []}])

s = fresh()
check("add scores 0 and 100 are allowed", lambda: add_student(s, {"id": 3, "name": "Bola", "scores": [0, 100]}), True,
      s, fresh() + [{"id": 3, "name": "Bola", "scores": [0, 100]}])

s = []
check("add to empty list", lambda: add_student(s, {"id": 1, "name": "Ada", "scores": [70]}), True,
      s, [{"id": 1, "name": "Ada", "scores": [70]}])

s = fresh()
check("add the same student twice: second is rejected", lambda: (add_student(s, bola), add_student(s, bola))[1], False,
      s, fresh() + [bola])

s = fresh()
check("add existing id with a different name", lambda: add_student(s, {"id": 1, "name": "Other", "scores": [10]}), False,
      s, fresh())

for bad in (None, "student", [1, "a", []], 5):
    s = fresh()
    check(f"add not a dict {bad!r}", lambda: add_student(s, bad), False, s, fresh())

for label, rec in [
    ("missing id", {"name": "B", "scores": [1]}),
    ("id is a string", {"id": "3", "name": "B", "scores": [1]}),
    ("id is a float", {"id": 3.0, "name": "B", "scores": [1]}),
    ("id is a bool", {"id": True, "name": "B", "scores": [1]}),
    ("id is None", {"id": None, "name": "B", "scores": [1]}),
    ("missing name", {"id": 3, "scores": [1]}),
    ("empty name", {"id": 3, "name": "", "scores": [1]}),
    ("whitespace-only name", {"id": 3, "name": "   ", "scores": [1]}),
    ("name is a number", {"id": 3, "name": 5, "scores": [1]}),
    ("name is None", {"id": 3, "name": None, "scores": [1]}),
    ("missing scores", {"id": 3, "name": "B"}),
    ("scores is None", {"id": 3, "name": "B", "scores": None}),
    ("scores is a string", {"id": 3, "name": "B", "scores": "80"}),
    ("scores is a tuple", {"id": 3, "name": "B", "scores": (80, 90)}),
    ("score above 100", {"id": 3, "name": "B", "scores": [50, 101]}),
    ("score negative", {"id": 3, "name": "B", "scores": [-1]}),
    ("score is a string", {"id": 3, "name": "B", "scores": ["80"]}),
    ("score is a bool", {"id": 3, "name": "B", "scores": [True]}),
    ("score is nan", {"id": 3, "name": "B", "scores": [NAN]}),
    ("score is None", {"id": 3, "name": "B", "scores": [None]}),
]:
    s = fresh()
    check(f"add rejects {label}", lambda: add_student(s, rec), False, s, fresh())

s = fresh()
original = {"id": 3, "name": "Bola", "scores": [50]}
add_student(s, original)
original["scores"].append(99)
original["name"] = "Changed"
check("add stores a copy (changing the original later does not change the stored one)",
      lambda: s[2], {"id": 3, "name": "Bola", "scores": [50]})

# ---------- find_student ----------
s = fresh()
check("find existing student", lambda: find_student(s, 2), TUNDE)
check("find returns the record itself, not a copy", lambda: find_student(s, 2) is s[1], True)
check("find first student", lambda: find_student(s, 1), ADA)
check("find id that does not exist", lambda: find_student(s, 99), None)
check("find in empty list", lambda: find_student([], 1), None)
check("find with id as string", lambda: find_student(s, "1"), None)
check("find with id as float", lambda: find_student(s, 1.0), None)
check("find with id True", lambda: find_student(s, True), None)
check("find with id None", lambda: find_student(s, None), None)
dupes = [{"id": 1, "name": "First", "scores": [1]}, {"id": 1, "name": "Second", "scores": [2]}]
check("find with duplicate ids in a hand-built list returns the first", lambda: find_student(dupes, 1)["name"], "First")

# ---------- calculate_average ----------
check("average example", lambda: calculate_average([80, 75, 90]), 81.67)
check("average other student", lambda: calculate_average([60, 85, 70]), 71.67)
check("average empty scores", lambda: calculate_average([]), 0)
check("average single score", lambda: calculate_average([100]), 100)
check("average all zeros", lambda: calculate_average([0, 0]), 0)
check("average rounds to 2 decimals", lambda: calculate_average([70, 70, 71]), 70.33)
check("average with decimals", lambda: calculate_average([50.5, 49.5]), 50.0)
check("average of two", lambda: calculate_average([1, 2]), 1.5)
for bad in ([101], [-1], [80, "x"], None, "80", [True], [NAN], [None], (80, 90), 80):
    check_raises(f"average rejects {bad!r}", lambda: calculate_average(bad))

# ---------- get_grade ----------
for avg, grade in [(100, "A"), (81.67, "A"), (70, "A"), (69.99, "B"), (60, "B"), (59.99, "C"), (50, "C"),
                   (49.99, "D"), (45, "D"), (44.99, "E"), (40, "E"), (39.99, "F"), (0, "F")]:
    check(f"grade for {avg}", lambda: get_grade(avg), grade)
for bad in (-1, 100.01, "80", None, True, NAN, [80]):
    check_raises(f"grade rejects {bad!r}", lambda: get_grade(bad))

# ---------- update_student_name ----------
s = fresh()
expected = fresh()
expected[1]["name"] = "Tunde Ade"
check("update name", lambda: update_student_name(s, 2, "Tunde Ade"), True, s, expected)

s = fresh()
expected = fresh()
expected[0]["name"] = "Ada Obi"
check("update strips the name", lambda: update_student_name(s, 1, "  Ada Obi "), True, s, expected)

s = fresh()
check("update to the same name", lambda: update_student_name(s, 1, "Ada"), True, s, fresh())

s = fresh()
check("update student that does not exist", lambda: update_student_name(s, 99, "Z"), False, s, fresh())
check("update in empty list", lambda: update_student_name([], 1, "Z"), False)
for bad in ("", "   ", "\n", None, 5, ["Ada"]):
    s = fresh()
    check(f"update rejects name {bad!r}", lambda: update_student_name(s, 1, bad), False, s, fresh())
for bad in ("1", 1.0, True, None):
    s = fresh()
    check(f"update rejects id {bad!r}", lambda: update_student_name(s, bad, "Z"), False, s, fresh())

# ---------- get_top_student ----------
s = fresh()
check("top student example", lambda: get_top_student(s), ADA, s, fresh())
check("top student when the best is last", lambda: get_top_student(list(reversed(fresh()))), ADA)
check("top student of one", lambda: get_top_student([TUNDE]), TUNDE)
check("top student of empty list", lambda: get_top_student([]), None)

tie = [{"id": 1, "name": "A", "scores": [70]}, {"id": 2, "name": "B", "scores": [80]}, {"id": 3, "name": "C", "scores": [80]}]
check("top student tie: first in list wins", lambda: get_top_student(tie)["id"], 2)
same = [{"id": 1, "name": "A", "scores": [80]}, {"id": 2, "name": "B", "scores": [90, 70]}]
check("top student tie on average (80 vs 80): first wins", lambda: get_top_student(same)["id"], 1)

by_total = [{"id": 1, "name": "A", "scores": [100]}, {"id": 2, "name": "B", "scores": [60, 60, 60]}]
check("top student uses average, not total", lambda: get_top_student(by_total)["id"], 1)

with_empty = [{"id": 1, "name": "A", "scores": []}, {"id": 2, "name": "B", "scores": [10]}]
check("top student: no scores counts as 0", lambda: get_top_student(with_empty)["id"], 2)
all_empty = [{"id": 1, "name": "A", "scores": []}, {"id": 2, "name": "B", "scores": []}]
check("top student: everyone has no scores, first wins", lambda: get_top_student(all_empty)["id"], 1)

check_raises("top student: a record has no scores field",
             lambda: get_top_student([{"id": 1, "name": "A", "scores": [50]}, {"id": 2, "name": "B"}]))
check_raises("top student: a record has a score above 100",
             lambda: get_top_student([{"id": 1, "name": "A", "scores": [50]}, {"id": 2, "name": "B", "scores": [101]}]))
check_raises("top student: a record has scores as a string",
             lambda: get_top_student([{"id": 1, "name": "A", "scores": "80"}]))

# ---------- get_students_above_average ----------
s = fresh()
check("above 75", lambda: get_students_above_average(s, 75), [ADA], s, fresh())
check("above 70 (both)", lambda: get_students_above_average(s, 70), [ADA, TUNDE])
check("above exactly Ada's average is strict", lambda: get_students_above_average(s, 81.67), [])
check("above 100", lambda: get_students_above_average(s, 100), [])
check("above -1 (everyone)", lambda: get_students_above_average(s, -1), [ADA, TUNDE])
check("above on empty list", lambda: get_students_above_average([], 50), [])
check("above 0 skips a student with no scores", lambda: get_students_above_average(with_empty, 0),
      [{"id": 2, "name": "B", "scores": [10]}])
ordered = [{"id": 1, "name": "A", "scores": [90]}, {"id": 2, "name": "B", "scores": [50]}, {"id": 3, "name": "C", "scores": [95]}]
check("above keeps list order", lambda: [x["id"] for x in get_students_above_average(ordered, 60)], [1, 3])
for bad in ("70", None, True, [70]):
    check_raises(f"above rejects threshold {bad!r}", lambda: get_students_above_average(fresh(), bad))
check_raises("above: a record has no scores field",
             lambda: get_students_above_average([{"id": 1, "name": "A"}], 50))
check_raises("above: a record has a negative score",
             lambda: get_students_above_average([{"id": 1, "name": "A", "scores": [-5]}], 50))

# ---------- remove_student ----------
def four():
    return [{"id": i, "name": f"S{i}", "scores": [i]} for i in (1, 2, 3, 4)]


s = four()
check("remove from the middle, others untouched", lambda: remove_student(s, 2), True, s,
      [{"id": 1, "name": "S1", "scores": [1]}, {"id": 3, "name": "S3", "scores": [3]}, {"id": 4, "name": "S4", "scores": [4]}])
s = four()
check("remove the first", lambda: remove_student(s, 1), True, s, four()[1:])
s = four()
check("remove the last", lambda: remove_student(s, 4), True, s, four()[:3])
s = fresh()
check("remove id that does not exist", lambda: remove_student(s, 99), False, s, fresh())
check("remove from empty list", lambda: remove_student([], 1), False)
for bad in ("1", 1.0, True, None):
    s = fresh()
    check(f"remove rejects id {bad!r}", lambda: remove_student(s, bad), False, s, fresh())

s = four()
check("remove twice: second time is False", lambda: (remove_student(s, 2), remove_student(s, 2))[1], False, s,
      [{"id": 1, "name": "S1", "scores": [1]}, {"id": 3, "name": "S3", "scores": [3]}, {"id": 4, "name": "S4", "scores": [4]}])

s = four()
remove_student(s, 3)
check("find after remove", lambda: find_student(s, 3), None)

s = [{"id": 1, "name": "First", "scores": [1]}, {"id": 1, "name": "Second", "scores": [2]}, {"id": 2, "name": "Other", "scores": [3]}]
check("remove with duplicate ids in a hand-built list removes only the first match", lambda: remove_student(s, 1), True, s,
      [{"id": 1, "name": "Second", "scores": [2]}, {"id": 2, "name": "Other", "scores": [3]}])

s = [{"id": 1, "name": "A", "scores": [1]}]
check("remove the only student", lambda: remove_student(s, 1), True, s, [])

print("BIM!!!" if failures == 0 else f"{failures} failed")