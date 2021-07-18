""" Vector
A vector data structure.
Example:
    $ from linear_algebra.vector import Vector
    $ vector = Vector([1,2,3])
"""

from __future__ import annotations
from typing import Union

from linear_algebra.array import Array


NumericType = Union[complex, float]
VectorType = list[NumericType]


class Vector(Array):
    '''Vector data structure'''

    def __init__(self, data: VectorType):
        super().__init__(data)
        if not self._valid_vector_shape():
            raise ValueError("Data is not a vector")

    def __repr__(self) -> str:
        if len(str(self.data)) < 64:
            representation = f"Vector {self.data} of shape {self.shape}"
        else:
            representation = f"Vector of shape {self.shape}"
        return representation

    def _valid_vector_shape(self) -> bool:
        """Checks whether a vector has a valid shape"""
        if len(self.shape) != 1:
            result = False
        else:
            result = True
        return result
