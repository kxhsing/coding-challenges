def print_matrix_spiral(matrix):
    """Given a m x n matrix (list of lists), print in spiral pattern
    e.g.:
    [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    will print to: 1 2 3 6 9 8 7 4 5

    """

    result = []
    if not matrix:
        return None

    while matrix:
        result += matrix.pop(0) #pop off and add entire first row

        if matrix and matrix[0]:
            for row in matrix:
                result.append(row.pop())

        if matrix:
            result += matrix.pop()[::-1]

        if matrix and matrix[0]:
            for row in matrix[::-1]:
                result.append(row.pop(0))

    return result





