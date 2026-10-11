from first_non_repeating import first_non_repeating

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
check("aabbcde",                   first_non_repeating("aabbcde"),         "c")
check("all repeating",             first_non_repeating("aabb"),            None)
check("single character",          first_non_repeating("z"),               "z")
check("case sensitive difference", first_non_repeating("aAbBc"),           "a")
check("empty string",              first_non_repeating(""),                None)

# ── edge cases ────────────────────────────────────────────────────────────────
check("swiss example",             first_non_repeating("swiss"),           "w")
check("all unique chars",          first_non_repeating("abcdef"),          "a")
check("answer is last char",       first_non_repeating("aabbccz"),         "z")
check("repeats around single",     first_non_repeating("racecar"),         "e")
check("digits in string",          first_non_repeating("1122344"),         "3")
check("middle single with spaces", first_non_repeating("a b a"),           "b")
check("space occurs once",         first_non_repeating("aa b"),            " ")

print(f"\ncore: {core_total - core_fail}/{core_total} passed")
if core_fail == 0:
    print("BIM!!!")

# ── bonus (case-insensitive) ──────────────────────────────────────────────────
check("case-insensitive aAbBc",    first_non_repeating("aAbBc", case_sensitive=False), "c",  bonus=True)
check("case-insensitive Aa",       first_non_repeating("Aa", case_sensitive=False),    None, bonus=True)
check("case-insensitive aabb",     first_non_repeating("aabb", case_sensitive=False),  None, bonus=True)

print(f"\nbonus: {bonus_total - bonus_fail}/{bonus_total} passed")
