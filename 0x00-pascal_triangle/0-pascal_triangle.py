#!/usr/bin/python3
""" Creates a function that returns a lits of lists
of integers representing the Pascal's triangle of n """


def pascal_triangle(n):
    """ creates a pascal triangle
    n:
        number of rows
    return:
        Pascal's triangle """
    new_pascal = []

    if n <= 0:
        return new_pascal

    for _ in range(n):
        row_index = [1]
        if new_pascal:
            final_row = new_pascal[-1]
            row_index.extend([sum(pair) for pair in
                              zip(final_row, final_row[1:])])
            row_index.append(1)
        new_pascal.append(row_index)
    return (new_pascal)
