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
        if len(self.shape) != 2:
            result = False
        else:
            result = True
        return result