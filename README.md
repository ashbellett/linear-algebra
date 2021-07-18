# Linear Algebra

Implementations of linear algebra algorithms

## Classes

### Array

Generic array data structure used as base class for matrix and vector classes
```python
from linear_algebra.array import Array

array = Array([[[1,2],[3,4]],[[5,6],[7,8]]])
array
# Array [[[1, 2], [3, 4]], [[5, 6], [7, 8]]] of shape (2, 2, 2)
```

`data`: Returns array data as a nested list
```python
array.data
# [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]
```

`shape`: Returns lengths of array dimensions. Uses a recursive implementation to calculate the array shape
```python
array.shape
# (2, 2, 2)
```

### Matrix

Matrix data structure; inherited from `Array` class
```python
from linear_algebra.matrix import Matrix

matrix = Matrix([[1,2],[3,4]])
matrix
# Matrix [[1, 2], [3, 4]] of shape (2, 2)
```

`is_square()`: Returns whether the matrix shape is square
```python
matrix.is_square()
# True
```

`determinant()`: Returns the matrix determinant. Uses a recursive Laplace expansion to calculate the determinant
```python
matrix.determinant()
# -2
```

`trace()`: Returns the matrix trace
```python
matrix.trace()
# 5
```

`transpose()`: Returns the matrix transpose
```python
matrix.transpose()
# Matrix [[1, 3], [2, 4]] of shape (2, 2)
```

`norm()`: Returns the Frobenius norm of the matrix
```python
matrix.norm()
# 5.477225575051661
```

`multiply()`: Returns the product of two matrices
```python
matrix.multiply(matrix)
# Matrix [[7, 10], [15, 22]] of shape (2, 2)
```

### Vector

Vector data structure; inherited from `Array` class
```python
from linear_algebra.vector import Vector

vector = Vector([1,2,3])
vector
# Vector [1, 2, 3] of shape (3,)
```

## Backlog

### Matrix Properties
- Rank
- Rowspace
- Columnspace
- Nullspace
- Definiteness

### Products
- Vector inner product
- Vector outer product
- Kronecker product

### Decompositions
- LU decomposition
- Rank factorisation
- Cholesky decomposition
- QR decomposition
- Eigendecomposition
- Jordan decomposition
- Schur decomposition
- Singular value decomposition

### Transformations
- Gram-Schmidt orthogonalisation
- Matrix projection
- Matrix inverses