# Linear Algebra

Implementations of linear algebra algorithms

## Classes

### Array

Generic array data structure used as base class for matrix and vector classes

#### Data
Returns array data as a list
```
array = Array([[1,2],[3,4]])
array.data
# [[1,2],[3,4]]
```

#### Shape
Returns lengths of array dimensions
```
array = Array([[1,2],[3,4]])
array.shape
# (2,2)
```

### Matrix

Matrix data structure; inherited from Array class

### Vector

Vector data structure; inherited from Array class

## Backlog

### Matrix Properties
- Determinant
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