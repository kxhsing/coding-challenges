def rotate_matrix_90(matrix):
    """Given a matrix of size mxn, print matrix rotated by 90 degrees"""

    matrix[:] = [[row[i] for row in matrix[::-1]] for i in range(len(matrix))]

    return matrix