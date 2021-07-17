""" Matrix
A matrix data structure.
Example:
    $ from linear_algebra.matrix import Matrix
    $ matrix = Matrix([[1,2],[3,4]])
"""

from __future__ import annotations
from typing import Union

from linear_algebra.array import Array


NumericType = Union[complex, float, int]
MatrixType = list[NumericType]


class Matrix(Array):
    '''Matrix data structure'''

    def __init__(self, data: MatrixType):
        super().__init__(data)
        if not self._valid_matrix_shape():
            raise ValueError("Data is not a matrix")

    def __repr__(self) -> str:
        if len(str(self.data)) < 64:
            representation = f"Matrix {self.data} of shape {self.shape}"
        else:
            representation = f"Matrix of shape {self.shape}"
        return representation

    def _valid_matrix_shape(self) -> bool:
        """Checks whether a matrix has a valid shape"""
        if len(self.shape) != 2:
            valid = False
        else:
            valid = True
        return valid

    def is_square(self) -> bool:
        """Checks whether a matrix' shape is square"""
        if self.shape[0] == self.shape[1]:
            result = True
        else:
            result = False
        return result

    def determinant(self) -> float:
        """Calculates the determinant of a matrix"""
        result = self._determinant(self.data)
        return result

    def _determinant(self, matrix: MatrixType) -> float:
        """Performs Laplace expansion to calculate the matrix determinant"""
        if not self.is_square():
            raise ValueError("Matrix is not square")
        if len(matrix) == 1:
            return matrix[0][0]
        determinant = 0
        for column, element in enumerate(matrix[0]):
            minor = [sub_matrix[:column] + sub_matrix[column + 1:] for sub_matrix in matrix[1:]]
            sign = 1 if column % 2 == 0 else -1
            determinant += sign * element * self._determinant(minor)
        return determinant
