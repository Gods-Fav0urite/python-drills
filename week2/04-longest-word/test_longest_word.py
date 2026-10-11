from longest_word import longest_word, longest_words

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
check("quick brown fox",             longest_word("the quick brown fox"),              "quick")
check("hi there",                    longest_word("hi there"),                         "there")
check("tie goes to first",           longest_word("cat bat rat"),                      "cat")
check("punctuation stripped",        longest_word("hello, world"),                     "hello")
check("empty string",                longest_word(""),                                 "")

# ── edge cases ────────────────────────────────────────────────────────────────
check("spaces only",                 longest_word("     "),                            "")
check("single word",                 longest_word("Python"),                           "Python")
check("problem description example", longest_word("Python makes problem solving fun"), "problem")
check("punctuation-only tokens",     longest_word("--- ... !?"),                       "")
check("token emptied by strip",      longest_word("hello --- world"),                  "hello")
check("numbers in sentence",         longest_word("I ran 123 kilometres"),             "kilometres")
check("multiple punctuation",        longest_word("...hello... world!"),               "hello")
check("internal hyphens kept",       longest_word("a well-known actor"),               "well-known")
check("multiple spaces",             longest_word("the   quick   brown"),              "quick")

print(f"\ncore: {core_total - core_fail}/{core_total} passed")
if core_fail == 0:
    print("BIM!!!")

# ── bonus (return all tied words) ─────────────────────────────────────────────
check("bonus: all 3 tie",            longest_words("cat bat rat"),                     ["cat", "bat", "rat"],  bonus=True)
check("bonus: two tied for longest", longest_words("the quick brown fox"),             ["quick", "brown"],     bonus=True)
check("bonus: single winner",        longest_words("hi there"),                        ["there"],              bonus=True)
check("bonus: empty input",          longest_words(""),                                [],                     bonus=True)
check("bonus: multiple spaces",      longest_words("the   quick   fox"),               ["quick"],              bonus=True)

print(f"\nbonus: {bonus_total - bonus_fail}/{bonus_total} passed")
