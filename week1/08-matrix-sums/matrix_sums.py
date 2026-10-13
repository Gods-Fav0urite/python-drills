def matrix_sums(matrix):
    if not matrix:
        return ([], [])
    row_sums = []
    num_columns = len(matrix[0])
    col_sums = [0] * num_columns

    for row in matrix:
        current_row_total = 0
        for col_index, value in enumerate(row):
            current_row_total += value
            col_sums[col_index] += value
        row_sums.append(current_row_total)

    return (row_sums, col_sums)