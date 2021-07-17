# Linear Algebra

Implementations of linear algebra algorithms

## Array

Generic array data structure used as base class for matrix and vector classes

### Data
Returns array data as a list
```
array = Array([[1,2],[3,4]])
array.data
# [[1,2],[3,4]]
```

### Shape
Returns lengths of array dimensions
```
array = Array([[1,2],[3,4]])
array.shape
# (2,2)
```

## Matrix

Matrix data structure; inherited from Array class

## Vector

Vector data structure; inherited from Array class
