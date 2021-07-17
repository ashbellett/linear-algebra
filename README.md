# Linear Algebra

Implementations of linear algebra algorithms

## Classes

### Array

Generic array data structure used as base class for matrix and vector classes
```python
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

### Vector

Vector data structure; inherited from `Array` class

## Backlog

### Matrix Properties
- Transpose
- Norm
- Rank
- Trace
- Rowspace
- Columnspace
- Nullspace
- Definiteness

### Products
- Inner product
- Outer product
- Matrix multiplication
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