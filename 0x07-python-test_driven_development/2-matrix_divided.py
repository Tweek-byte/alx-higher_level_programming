def matrix_divided(matrix, div):
    """Divides matrix by scalar integer, rounded to two decimal places."""

    err = "matrix must be a matrix (list of lists) of integers/floats"

    if not isinstance(matrix, list):
        raise TypeError(err)

    row_len = set()
    for row in matrix:
        if not isinstance(row, list):
            raise TypeError(err)
        row_len.add(len(row))
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError(err)

    if len(row_len) > 1:
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    def divide_and_round(x):
        return round(x / div, 2)

    new_matrix = [list(map(divide_and_round, row)) for row in matrix]
    return new_matrix
