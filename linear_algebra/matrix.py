""" Matrix
A matrix data structure.
Example:
    $ from linear_algebra.matrix import Matrix
    $ matrix = Matrix([[1,2],[3,4]])
"""

from __future__ import annotations
import math
from typing import Union

from linear_algebra.array import Array


NumericType = Union[complex, float]
MatrixType = list[list[NumericType]]


class Matrix(Array):
    """Matrix data structure"""

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
        """Check whether a matrix has a valid shape"""
        valid = len(self.shape) == 2
        return valid

    def is_square(self) -> bool:
        """Check whether a matrix is square"""
        result = self.shape[0] == self.shape[1]
        return result

    def is_identity(self) -> bool:
        """Check whether a matrix is an identity matrix"""
        if not self.is_square():
            raise ValueError("Matrix is not square")
        for row in range(self.shape[0]):
            for column in range(self.shape[1]):
                if (row == column) and self.data[row][column] != 1:
                    return False
                if (row != column) and self.data[row][column] != 0:
                    return False
        return True

    def determinant(self) -> NumericType:
        """Calculate the determinant of a matrix"""
        result = self._determinant(self.data)
        return result

    def _determinant(self, matrix: MatrixType) -> NumericType:
        """Perform Laplace expansion to calculate the matrix determinant"""
        if not self.is_square():
            raise ValueError("Matrix is not square")
        if len(matrix) == 1:
            return matrix[0][0]
        determinant = 0.0
        for column, element in enumerate(matrix[0]):
            minor = [
                sub_matrix[:column] + sub_matrix[column + 1:]
                for sub_matrix in matrix[1:]
            ]
            sign = 1 if column % 2 == 0 else -1
            determinant += sign * element * self._determinant(minor)
        return determinant

    def trace(self) -> NumericType:
        """Calculate the trace of a matrix"""
        if not self.is_square():
            raise ValueError("Matrix is not square")
        trace = 0.0
        for diagonal in range(self.shape[0]):
            trace += self.data[diagonal][diagonal]
        return trace

    def transpose(self) -> Matrix:
        """Calculate the transpose of a matrix"""
        transpose = [list(row) for row in zip(*self.data)]
        return Matrix(transpose)

    def is_symmetric(self) -> bool:
        """Check whether a matrix is symmetric"""
        result = self.data == self.transpose().data
        return result

    def norm(self) -> NumericType:
        """Calculate the Frobenius norm of a matrix"""
        norm = 0.0
        for row in range(self.shape[0]):
            for column in range(self.shape[1]):
                norm += pow(self.data[row][column], 2)
        norm = math.sqrt(norm)
        return norm

    def multiply(self, other: Matrix) -> Matrix:
        """Calculate the product of two matrices"""
        if self.shape[1] != other.shape[0]:
            raise ValueError("Matrix dimensions are incompatible")
        product = [
            [
                sum(
                    left_element * right_element
                    for left_element, right_element
                    in zip(left_row, right_column)
                )
                for right_column in zip(*other.data)
            ]
            for left_row in self.data
        ]
        return Matrix(product)

    def is_orthogonal(self) -> bool:
        """Check whether a matrix is orthogonal"""
        transpose = self.transpose()
        product = self.multiply(transpose)
        result = product.is_identity()
        return result
