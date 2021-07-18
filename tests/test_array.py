from unittest import TestCase

from linear_algebra.array import Array
from tests.data.tensor import (
    tensor_data,
    tensor_shape
)

class TestArray(TestCase):

    def setUp(self) -> None:
        self.array = Array(tensor_data)

    def test_data(self):
        self.assertEqual(self.array.data, tensor_data)

    def test_shape(self):
        self.assertEqual(self.array.shape, tensor_shape)
