def most_frequent(items):
    if not items:
        return None

    frequencies = {}
    for item in items:
        if item in frequencies:
            frequencies[item] += 1
        else:
            frequencies[item] = 1

    most_frequent_item = items[0]
    max_frequency = frequencies[most_frequent_item]
    for item, frequency in frequencies.items():
        if frequency > max_frequency:
            most_frequent_item = item
            max_frequency = frequency   

    return most_frequent_item