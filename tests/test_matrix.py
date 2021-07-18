from unittest import TestCase

from linear_algebra.matrix import Matrix
from tests.data.matrix import matrix_data, matrix_shape


class TestMatrix(TestCase):
    def setUp(self) -> None:
        self.matrix = Matrix(matrix_data)

    def test_data(self):
        self.assertEqual(self.matrix.data, matrix_data)

    def test_shape(self):
        self.assertEqual(self.matrix.shape, matrix_shape)
