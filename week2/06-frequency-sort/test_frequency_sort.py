from frequency_sort import frequency_sort

core_total = 0
core_fail = 0
bonus_total = 0
bonus_fail = 0


def check(label, got, expected, bonus=False):
    global core_total, core_fail, bonus_total, bonus_fail
    if bonus:
        bonus_total += 1
        if got != expected:
            bonus_fail += 1
            print(f"FAIL [{label}]")
            print(f"  expected: {expected!r}")
            print(f"  got:      {got!r}\n")
    else:
        core_total += 1
        if got != expected:
            core_fail += 1
            print(f"FAIL [{label}]")
            print(f"  expected: {expected!r}")
            print(f"  got:      {got!r}\n")


# ── examples from spec ─────────────────────────────────────────────────────────
check("spec example 1",             frequency_sort([4, 5, 6, 5, 4, 4]),             [4, 4, 4, 5, 5, 6])
check("spec example 2",             frequency_sort([1, 2, 2, 1, 3]),                [1, 1, 2, 2, 3])
check("single element",             frequency_sort([5]),                            [5])
check("empty list",                 frequency_sort([]),                             [])

# ── requirements & edge cases ─────────────────────────────────────────────────
check("equal frequencies tie",      frequency_sort([3, 3, 1, 1, 2]),                [1, 1, 3, 3, 2])
check("all unique descending",      frequency_sort([5, 4, 3, 2, 1]),                [1, 2, 3, 4, 5])
check("all same element",           frequency_sort([7, 7, 7, 7]),                   [7, 7, 7, 7])
check("negatives and zeros",        frequency_sort([0, 0, -1, -1, -1]),             [-1, -1, -1, 0, 0])
check("two pairs and one",          frequency_sort([4, 1, 4, 1, 2, 2]),             [1, 1, 2, 2, 4, 4])
check("multi-frequency tie-break",  frequency_sort([4, 4, 1, 2, 2, 2, 3, 3, 5]),   [2, 2, 2, 3, 3, 4, 4, 1, 5])

# ── do not mutate original list ───────────────────────────────────────────────
orig = [3, 1, 2]
res = frequency_sort(orig)
check("does not mutate original list", orig == [3, 1, 2] and res is not orig,       True)

print(f"\ncore: {core_total - core_fail}/{core_total} passed")
if core_fail == 0:
    print("BIM!!!")

# ── bonus (strings) ───────────────────────────────────────────────────────────
check("bonus: list of strings",     frequency_sort(["banana", "apple", "apple", "cherry"]), ["apple", "apple", "banana", "cherry"], bonus=True)
check("bonus: strings alphabetical tie", frequency_sort(["b", "a", "c"]),                   ["a", "b", "c"],                         bonus=True)

print(f"\nbonus: {bonus_total - bonus_fail}/{bonus_total} passed")
