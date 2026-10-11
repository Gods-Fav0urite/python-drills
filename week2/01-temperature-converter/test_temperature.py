import math

from temperature import (
    celsius_to_fahrenheit,
    fahrenheit_to_celsius,
    celsius_to_kelvin,
    convert_temperature,
)

# results are floats, so we compare with math.isclose instead of ==
# convert_temperature must raise ValueError for bad input (units, non-numbers, below absolute zero)


def close(got, expected):
    return isinstance(got, (int, float)) and math.isclose(got, expected, abs_tol=1e-9)


def outcome(fn, *args):
    try:
        return fn(*args)
    except ValueError:
        return "ValueError"
    except Exception as error:
        return type(error).__name__


celsius_to_fahrenheit_tests = [
    (32, 0),          # freezing point
    (212, 100),       # boiling point
    (-40, -40),       # same in both scales
    (98.6, 37),       # body temperature
    (-459.67, -273.15),  # absolute zero
]

fahrenheit_to_celsius_tests = [
    (0, 32),
    (100, 212),
    (-40, -40),
    (37, 98.6),
    (-273.15, -459.67),
]

celsius_to_kelvin_tests = [
    (273.15, 0),
    (373.15, 100),
    (233.15, -40),
    (0, -273.15),     # absolute zero
]

# (expected, value, from_unit, to_unit)
convert_tests = [
    (32, 0, "celsius", "fahrenheit"),       # 0C to F, from the problem
    (-40, -40, "celsius", "fahrenheit"),    # -40C to F, from the problem
    (373.15, 100, "celsius", "kelvin"),     # 100C to K, from the problem
    (0, 32, "fahrenheit", "celsius"),
    (273.15, 32, "fahrenheit", "kelvin"),
    (0, 273.15, "kelvin", "celsius"),
    (32, 273.15, "kelvin", "fahrenheit"),
    (25, 25, "celsius", "celsius"),         # same unit returns the original value
    (77, 77, "fahrenheit", "fahrenheit"),
    (300, 300, "kelvin", "kelvin"),
    (32, 0, "CELSIUS", "Fahrenheit"),       # unit names ignore case
    (0, -273.15, "celsius", "kelvin"),      # exactly absolute zero is allowed
    (-273.15, 0, "kelvin", "celsius"),
    (-273.15, -459.67, "fahrenheit", "celsius"),
]

# (value, from_unit, to_unit), each must raise ValueError
error_tests = [
    (25, "rankine", "celsius"),             # unknown from unit
    (25, "celsius", "rankine"),             # unknown to unit
    (25, "", "celsius"),                    # empty unit
    (25, None, "celsius"),                  # unit is not a string
    (-273.16, "celsius", "kelvin"),         # below absolute zero
    (-459.68, "fahrenheit", "celsius"),
    (-1, "kelvin", "celsius"),
    (-300, "celsius", "celsius"),           # same unit, still invalid
    ("25", "celsius", "fahrenheit"),        # numeric string is rejected
    ("", "celsius", "fahrenheit"),          # empty string
    ("abc", "celsius", "fahrenheit"),       # non-numeric
    (None, "celsius", "fahrenheit"),
    (True, "celsius", "fahrenheit"),        # True is not a temperature
]

failures = 0

for name, fn, table in [
    ("celsius_to_fahrenheit", celsius_to_fahrenheit, celsius_to_fahrenheit_tests),
    ("fahrenheit_to_celsius", fahrenheit_to_celsius, fahrenheit_to_celsius_tests),
    ("celsius_to_kelvin", celsius_to_kelvin, celsius_to_kelvin_tests),
]:
    for expected, value in table:
        got = fn(value)
        if not close(got, expected):
            failures += 1
            print(f"FAIL: {name}({value!r})")
            print(f"  expected: {expected}")
            print(f"  got:      {got!r}\n")

for expected, value, from_unit, to_unit in convert_tests:
    got = outcome(convert_temperature, value, from_unit, to_unit)
    if not close(got, expected):
        failures += 1
        print(f"FAIL: convert_temperature({value!r}, {from_unit!r}, {to_unit!r})")
        print(f"  expected: {expected}")
        print(f"  got:      {got!r}\n")

for value, from_unit, to_unit in error_tests:
    got = outcome(convert_temperature, value, from_unit, to_unit)
    if got != "ValueError":
        failures += 1
        print(f"FAIL: convert_temperature({value!r}, {from_unit!r}, {to_unit!r})")
        print("  expected: raises ValueError")
        print(f"  got:      {got!r}\n")

print("BIM!!!" if failures == 0 else f"{failures} failed")