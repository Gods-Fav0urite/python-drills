def count_characters(text):
    counts = {
        "letters": 0,
        "numbers": 0,
        "spaces": 0,
        "special": 0
    }

    for char in text:
        if char.isalpha():
            counts["letters"] += 1
        elif char.isdigit():
            counts["numbers"] += 1
        elif char == " ":
            counts["spaces"] += 1
        else:
            counts["special"] += 1

    return counts