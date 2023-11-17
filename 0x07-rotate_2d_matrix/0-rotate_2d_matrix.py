#!/usr/bin/python3
""" Rotate a 2d Matrix """


def rotate_2d_matrix(matrix):
    """
    Rotate a Matrix 90 deg
    The Rotated Matrix is an image of the matrix with:
        * Each vector containing elemets that belonged to vecotrs
        * Each Elemets included in one vectors add previously the same
        index in the normal Matrix.
        * (There is also a revers aspect)
    """
    rotated_matrix = []
    vector_items = len(matrix[0])

    for idx in range(0, vector_items):
        """
        * Loop over the matrix
        * Add the element with Id == iteration:
        * reverse the vector
        * Add it to the rotated_matrix
        """

        new_vector = []

        for vector_id in range(len(matrix)):
            vector_id_to_choose = len(matrix) - 1 - vector_id
            new_vector.append(matrix[vector_id_to_choose][idx])

        rotated_matrix.append(new_vector)

    matrix[:] = rotated_matrix
