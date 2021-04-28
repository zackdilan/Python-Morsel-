"""
Hey! ✨

I'd like you to write a function that accepts two lists-of-lists of numbers and returns one list-of-lists with each of the corresponding numbers in the two given lists-of-lists added together.

It should work something like this:

>>> matrix1 = [[1, -2], [-3, 4]]
>>> matrix2 = [[2, -1], [0, -1]]
>>> add(matrix1, matrix2)
[[3, -3], [-3, 3]]
>>> matrix1 = [[1, -2, 3], [-4, 5, -6], [7, -8, 9]]
>>> matrix2 = [[1, 1, 0], [1, -2, 3], [-2, 2, -2]]
>>> add(matrix1, matrix2)
[[2, -1, 3], [-3, 3, -3], [5, -6, 7]]
"""


def add(matrix1, matrix2):
    """

    :param matrix1:
    :param matrix2:
    :return:
    """

    return [[(x + y) for x, y in zip(list_matrix1, list_matrix2)] for (list_matrix1, list_matrix2) in
            zip(matrix1, matrix2)]


def add_multiple_args(*args):
    print((args))

    # return [[(x + y) for x, y in zip(list_matrix)] for (list_matrix) in
    #         zip(args)]


if __name__ == "__main__":
    matrix1 = [[1, -2], [-3, 4]]
    matrix2 = [[2, -1], [0, -1]]
    (add_multiple_args(matrix1, matrix2))
