from unittest import TestCase

from linear_algebra.vector import Vector
from tests.data import (
    vector_data,
    vector_shape
)

class TestVector(TestCase):

    def setUp(self) -> None:
        self.vector = Vector(vector_data)

    def test_data(self):
        self.assertEqual(self.vector.data, vector_data)

    def test_shape(self):
        self.assertEqual(self.vector.shape, vector_shape)
