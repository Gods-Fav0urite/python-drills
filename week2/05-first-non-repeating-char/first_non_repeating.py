def first_non_repeating(s, case_sensitive=True):
    if not s:
        return None

    char_counts = {}
    processed_chars = []

    for char in s:
        key = char if case_sensitive else char.lower()
        if key in char_counts:
            char_counts[key] += 1
        else:
            char_counts[key] = 1
            processed_chars.append((char, key))
            
    for original_char, key in processed_chars:
        if char_counts[key] == 1:
            return original_char

    return None