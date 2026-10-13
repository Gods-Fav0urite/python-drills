def intersection(a, b):
    result = []

    for item in a:
        if item in b and item not in result:
            result.append(item)
    return result
