from unittest import TestCase

from linear_algebra.matrix import Matrix
from tests.data.matrix import (
    matrix_data,
    matrix_shape,
    matrix_is_square,
    matrix_determinant,
    matrix_trace,
    matrix_transpose,
    matrix_norm,
    matrix_product
)


class TestMatrix(TestCase):
    def setUp(self) -> None:
        self.matrix = Matrix(matrix_data)

    def test_data(self):
        self.assertEqual(self.matrix.data, matrix_data)

    def test_shape(self):
        self.assertEqual(self.matrix.shape, matrix_shape)

    def test_is_square(self):
        self.assertEqual(self.matrix.is_square(), matrix_is_square)

    def test_determinant(self):
        self.assertEqual(self.matrix.determinant(), matrix_determinant)

    def test_trace(self):
        self.assertEqual(self.matrix.trace(), matrix_trace)

    def test_transpose(self):
        self.assertEqual(
            self.matrix.transpose().data,
            matrix_transpose
        )

    def test_norm(self):
        self.assertEqual(
            round(self.matrix.norm(), 12),
            matrix_norm
        )

    def test_product(self):
        self.assertEqual(
            self.matrix.multiply(self.matrix).data,
            matrix_product
        )
