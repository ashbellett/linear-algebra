""" Vector
A vector data structure.
Example:
    $ from linear_algebra.vector import Vector
    $ vector = Vector([[1,2],[3,4]])
"""

from __future__ import annotations
from typing import Union

from linear_algebra.array import Array


NumericType = Union[complex, float, int]
VectorType = list[NumericType]


class Vector(Array):
    '''Vector data structure'''

    def __init__(self, data: VectorType):
        super().__init__(data)
        if not self._valid_vector_shape():
            raise ValueError("Data is not a vector")

    def _valid_vector_shape(self) -> bool:
        if len(self.shape) != 1:
            result = False
        else:
            result = True
        return result
