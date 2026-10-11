import io
import unittest.mock
from contextlib import redirect_stdout

from number_guessing_game import play_game

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


def run_game(inputs, target=37, max_attempts=None):
    it = iter(inputs)

    def mock_input(prompt=""):
        try:
            return next(it)
        except StopIteration:
            raise EOFError("No more mock inputs provided")

    captured = io.StringIO()
    with redirect_stdout(captured):
        with unittest.mock.patch("builtins.input", side_effect=mock_input):
            with unittest.mock.patch("random.randint", return_value=target):
                try:
                    if max_attempts is not None:
                        play_game(target=target, max_attempts=max_attempts)
                    else:
                        play_game(target=target)
                except TypeError:
                    play_game()
                except EOFError:
                    pass
    return captured.getvalue()


# ── core gameplay ─────────────────────────────────────────────────────────────
out1 = run_game(["37"], target=37)
check("immediate correct guess", "correct! you got it in 1 guesses" in out1.lower(), True)

out2 = run_game(["50", "37"], target=37)
check("feedback too high", "too high" in out2.lower(), True)
check("count 2 guesses after too high", "correct! you got it in 2 guesses" in out2.lower(), True)

out3 = run_game(["25", "37"], target=37)
check("feedback too low", "too low" in out3.lower(), True)
check("count 2 guesses after too low", "correct! you got it in 2 guesses" in out3.lower(), True)

# ── input validation ──────────────────────────────────────────────────────────
out4 = run_game(["hello", "37"], target=37)
check("invalid non-integer error", "invalid" in out4.lower(), True)
check("invalid non-integer not counted", "correct! you got it in 1 guesses" in out4.lower(), True)

out5 = run_game(["3.5", "37"], target=37)
check("decimal error", "invalid" in out5.lower(), True)
check("decimal not counted", "correct! you got it in 1 guesses" in out5.lower(), True)

out6 = run_game(["", "   ", "37"], target=37)
check("empty string not counted", "correct! you got it in 1 guesses" in out6.lower(), True)

out7 = run_game(["0", "-5", "37"], target=37)
check("numbers below 1 not counted", "correct! you got it in 1 guesses" in out7.lower(), True)

out8 = run_game(["101", "200", "37"], target=37)
check("numbers above 100 not counted", "correct! you got it in 1 guesses" in out8.lower(), True)

# ── boundary and example session ──────────────────────────────────────────────
out9 = run_game(["1", "100", "50"], target=50)
check("1 is too low", "too low" in out9.lower(), True)
check("100 is too high", "too high" in out9.lower(), True)
check("boundaries 1 and 100 are valid guesses", "correct! you got it in 3 guesses" in out9.lower(), True)

out10 = run_game(["hello", "50", "25", "37"], target=37)
check("example session ends in 3 guesses", "correct! you got it in 3 guesses" in out10.lower(), True)

print(f"\ncore: {core_total - core_fail}/{core_total} passed")
if core_fail == 0:
    print("BIM!!!")

# ── bonus ─────────────────────────────────────────────────────────────────────
out_bonus1 = run_game(["10", "20", "30"], target=77, max_attempts=3)
check("max attempts reveals number", "77" in out_bonus1, True, bonus=True)

print(f"\nbonus: {bonus_total - bonus_fail}/{bonus_total} passed")
