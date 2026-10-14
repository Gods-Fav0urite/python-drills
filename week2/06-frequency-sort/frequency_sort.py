def frequency_sort(items):
  counts = {}
  for item in items:
    counts[item] = counts.get(item, 0) + 1

  return sorted(items, key=lambda x: (-counts[x], x))
