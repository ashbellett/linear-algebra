# Linear Algebra

Implementations of linear algebra algorithms

## Classes

### Array

Generic array data structure used as base class for matrix and vector classes
```
array = Array([[[1,2],[3,4]],[[5,6],[7,8]]])
```

`data`
Returns array data as a list
```
array.data
# [[[1,2],[3,4]],[[5,6],[7,8]]]
```

`shape`
Returns lengths of array dimensions
```
array.shape
# (2,2,2)
```

### Matrix

Matrix data structure; inherited from Array class
```
matrix = Matrix([[1,2],[3,4]])
```

`is_square()`
Returns whether the matrix shape is square
```
matrix.is_square()
# True
```

`determinant()`
Returns the matrix determinant. Uses a Laplace expansion to calculate the determinant
```
matrix.determinant()
# -6
```

### Vector

Vector data structure; inherited from Array class

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