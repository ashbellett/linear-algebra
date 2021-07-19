""" Array
A generic array data structure.
Used as a base class for vector and matrix classes.
Example:
    $ from linear_algebra.array import Array
    $ array = Array([[1,2],[3,4]])
"""

from __future__ import annotations
from typing import Union


NumericType = Union[complex, float]
ArrayType = Union[list[NumericType], NumericType]


class Array:
    """Generic array data structure"""

    def __init__(self, data: ArrayType) -> None:
        if not self._valid_shape(data):
            raise ValueError("Dimension mismatch within array")
        self.data = data
        self.shape = self._shape(data, [])

    def __repr__(self) -> str:
        if len(str(self.data)) < 64:
            representation = f"Array {self.data} of shape {self.shape}"
        else:
            representation = f"Array of shape {self.shape}"
        return representation

    def __len__(self) -> int:
        length = self.shape[0]
        return length

    def __getitem__(self, index) -> ArrayType:
        if len(self.shape) >= 1:
            result = self.data[index]
        else:
            raise IndexError("Array is a scalar value")
        return result

    def __setitem__(self, index, value: ArrayType) -> None:
        if len(self.shape) >= 1:
            prior_data = self.data
            prior_data[index] = value
            if not self._valid_shape(prior_data):
                raise ValueError("Dimension mismatch within array")
            self.data = prior_data
            self.shape = self._shape(prior_data, [])
        else:
            raise IndexError("Array is a scalar value")

    def __add__(self, other: Array) -> Array:
        if self.shape != other.shape:
            raise ValueError("Array dimensions do not match")
        result = self._add(self.data, other.data)
        return Array(result)

    def __sub__(self, other: Array) -> Array:
        if self.shape != other.shape:
            raise ValueError("Array dimensions do not match")
        result = self._sub(self.data, other.data)
        return Array(result)

    def _add(self, array: ArrayType, other: ArrayType) -> ArrayType:
        """Add the elements of two arrays"""
        if isinstance(array, list):
            results = []
            for array_item, other_item in zip(array, other):
                if isinstance(array_item, list):
                    result = self._add(array_item, other_item)
                    results.append(result)
                else:
                    result = array_item + other_item
                    results.append(result)
        else:
            results = array + other
        return results

    def _sub(self, array: ArrayType, other: ArrayType) -> ArrayType:
        """Subtract the elements of two arrays"""
        if isinstance(array, list):
            results = []
            for array_item, other_item in zip(array, other):
                if isinstance(array_item, list):
                    result = self._sub(array_item, other_item)
                    results.append(result)
                else:
                    result = array_item - other_item
                    results.append(result)
        else:
            results = array - other
        return results

    def _valid_shape(self, data: ArrayType) -> bool:
        """Check whether an array has a valid shape"""
        if isinstance(data, list):
            prior_length = None
            for item in data:
                if isinstance(item, list):
                    item_length = len(item)
                else:
                    item_length = 0
                if prior_length is None:
                    prior_length = item_length
                if item_length != prior_length:
                    return False
                result = self._valid_shape(item)
                if not result:
                    return False
        return True

    def _shape(self, data: ArrayType, shape: list[int]) -> tuple[int, ...]:
        """Get the shape of an array"""
        if isinstance(data, list):
            outer_length = len(data)
            shape.append(outer_length)
            if outer_length == 0:
                return tuple(shape)
            result = self._shape(data[0], shape)
            if isinstance(result, tuple):
                return result
        return tuple(shape)
