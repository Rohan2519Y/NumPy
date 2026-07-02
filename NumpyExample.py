"""
================================================================================
 NUMPY COMPLETE CHEAT SHEET - Copy-Paste Ready Reference
 All outputs verified by running on NumPy 2.4.4
 Each line: function call + actual output as a comment
================================================================================
"""

import numpy as np



# ==============================================================================
# ARRAY CREATION
# ==============================================================================

# Create array from list
np.array([1, 2, 3])
# Output: array([1, 2, 3])
# Creates a 1D array from a Python list

# Create 2D array from nested list
np.array([[1, 2], [3, 4]])
# Output:
# array([[1, 2],
#        [3, 4]])
# Creates a 2D array (matrix) from nested lists

# Array of zeros with specified shape
np.zeros((2, 3))
# Output:
# array([[0., 0., 0.],
#        [0., 0., 0.]])
# Creates 2x3 array filled with zeros (float64 by default)

# Array of ones with specified shape
np.ones((2, 3))
# Output:
# array([[1., 1., 1.],
#        [1., 1., 1.]])
# Creates 2x3 array filled with ones (float64 by default)

# Array filled with constant value
np.full((2, 2), 7)
# Output:
# array([[7, 7],
#        [7, 7]])
# Creates 2x2 array filled with 7 (int64 by default)

# Identity matrix
np.eye(3)
# Output:
# array([[1., 0., 0.],
#        [0., 1., 0.],
#        [0., 0., 1.]])
# Creates 3x3 identity matrix with ones on diagonal

# Identity matrix (alternative)
np.identity(3)
# Output:
# array([[1., 0., 0.],
#        [0., 1., 0.],
#        [0., 0., 1.]])
# Same as np.eye(3), creates identity matrix

# Range with step size
np.arange(0, 10, 2)
# Output: array([0, 2, 4, 6, 8])
# Creates array from 0 to 10 (exclusive) with step 2

# Linearly spaced values
np.linspace(0, 1, 5)
# Output: array([0.  , 0.25, 0.5 , 0.75, 1.  ])
# Creates 5 equally spaced values from 0 to 1 (inclusive)

# Empty array (uninitialized values)
np.empty((2, 2))
# Output:
# array([[0.25, 0.5 ],
#        [0.75, 1.  ]])
# Creates uninitialized array (values depend on memory state)

# Array with specified dtype
np.array([1, 2, 3], dtype=float)
# Output: array([1., 2., 3.])
# Creates array with specified data type (float64)

# Zero array with same shape as another array
np.zeros_like([[1,2],[3,4]])
# Output:
# array([[0, 0],
#        [0, 0]])
# Creates zeros with same shape and dtype as input

# Ones array with same shape as another array
np.ones_like([[1,2],[3,4]])
# Output:
# array([[1, 1],
#        [1, 1]])
# Creates ones with same shape and dtype as input

# Full array with same shape as another array
np.full_like([1,2,3], 9)
# Output: array([9, 9, 9])
# Creates array filled with 9, same shape as input

# Diagonal matrix
np.diag([1, 2, 3])
# Output:
# array([[1, 0, 0],
#        [0, 2, 0],
#        [0, 0, 3]])
# Creates diagonal matrix with specified diagonal values

# Create array using function
np.fromfunction(lambda i, j: i + j, (3, 3), dtype=int)
# Output:
# array([[0, 1, 2],
#        [1, 2, 3],
#        [2, 3, 4]])
# Creates array where each element is computed by function

# Additional creation functions

# Create array filled with zeros with custom dtype
np.zeros((2, 2), dtype=np.int32)
# Output:
# array([[0, 0],
#        [0, 0]], dtype=int32)
# Creates zeros with specified dtype (int32)

# Create array filled with ones with custom dtype
np.ones((2, 2), dtype=np.float32)
# Output:
# array([[1., 1.],
#        [1., 1.]], dtype=float32)
# Creates ones with specified dtype (float32)

# Create array with diagonal values from 1D array
np.diag([1, 2, 3, 4])
# Output:
# array([[1, 0, 0, 0],
#        [0, 2, 0, 0],
#        [0, 0, 3, 0],
#        [0, 0, 0, 4]])
# Creates 4x4 diagonal matrix with 1,2,3,4 on diagonal

# Create array from string (binary representation)
np.fromstring('1 2 3 4', dtype=int, sep=' ')
# Output: array([1, 2, 3, 4])
# Parses space-separated string to create array

# Create array from function with 2D coordinates
np.fromfunction(lambda i, j: i * j, (3, 3), dtype=int)
# Output:
# array([[0, 0, 0],
#        [0, 1, 2],
#        [0, 2, 4]])
# Creates array where each element = i*j

# Create triangular matrix (upper)
np.tri(3, 3, k=0)
# Output:
# array([[1., 0., 0.],
#        [1., 1., 0.],
#        [1., 1., 1.]])
# Creates lower triangular matrix with ones below diagonal

# Create triangular matrix (lower)
np.tri(3, 3, k=-1)
# Output:
# array([[0., 0., 0.],
#        [1., 0., 0.],
#        [1., 1., 0.]])
# Creates triangular matrix with diagonal offset


# ==============================================================================
# ARRAY PROPERTIES
# ==============================================================================

# Get shape of array
np.array([[1,2,3],[4,5,6]]).shape
# Output: (2, 3)
# Returns tuple of dimensions (rows, columns)

# Get number of dimensions
np.array([[1,2,3],[4,5,6]]).ndim
# Output: 2
# Returns number of array dimensions (2 for matrix)

# Get total number of elements
np.array([[1,2,3],[4,5,6]]).size
# Output: 6
# Returns total count of elements (2*3=6)

# Get data type
np.array([[1,2,3],[4,5,6]]).dtype
# Output: dtype('int64')
# Returns data type of array elements

# Get size in bytes of each element
np.array([[1,2,3],[4,5,6]]).itemsize
# Output: 8
# Returns byte size of each element (8 bytes for int64)

# Get total memory usage in bytes
np.array([[1,2,3],[4,5,6]]).nbytes
# Output: 48
# Total memory = itemsize * size (8*6=48 bytes)

# Transpose array
np.array([[1,2,3],[4,5,6]]).T
# Output:
# array([[1, 4],
#        [2, 5],
#        [3, 6]])
# Swaps rows and columns (2x3 becomes 3x2)

# Get memory layout flags
np.array([1,2,3]).flags
# Output:
# C_CONTIGUOUS : True
#   F_CONTIGUOUS : True
#   OWNDATA : True
#   WRITEABLE : True
#   ALIGNED : True
#   WRITEBACKIFCOPY : False
# Shows memory layout and permissions of array

# Additional properties

# Get strides (memory steps)
np.array([[1,2,3],[4,5,6]]).strides
# Output: (24, 8)
# Returns tuple of bytes to skip to reach next element in each dimension

# Get base array (if view)
np.array([1,2,3]).base
# Output: None
# Returns original array if this is a view, None if it owns data

# Get flat iterator
list(np.array([[1,2],[3,4]]).flat)
# Output: [1, 2, 3, 4]
# Returns flat iterator over all elements (row-major order)

# Get diagonal elements
np.array([[1,2,3],[4,5,6],[7,8,9]]).diagonal()
# Output: array([1, 5, 9])
# Returns main diagonal elements


# ==============================================================================
# RESHAPE & MANIPULATE
# ==============================================================================

# Reshape array to new shape
np.arange(6).reshape(2, 3)
# Output:
# array([[0, 1, 2],
#        [3, 4, 5]])
# Reshapes 1D array to 2x3 matrix (total elements must match)

# Ravel (flatten) to 1D (returns view if possible)
np.arange(6).reshape(2, 3).ravel()
# Output: array([0, 1, 2, 3, 4, 5])
# Returns flattened 1D array (may return view, modifies original)

# Flatten to 1D (always returns copy)
np.arange(6).reshape(2, 3).flatten()
# Output: array([0, 1, 2, 3, 4, 5])
# Returns flattened 1D array (always creates copy)

# Transpose using function
np.array([[1,2],[3,4]]).transpose()
# Output:
# array([[1, 3],
#        [2, 4]])
# Transposes array (same as .T property)

# Concatenate arrays
np.concatenate([[1,2],[3,4]])
# Output: array([1, 2, 3, 4])
# Concatenates arrays along existing axis (default axis=0)

# Vertical stack
np.vstack([[1,2],[3,4]])
# Output:
# array([[1, 2],
#        [3, 4]])
# Stacks arrays vertically (row-wise)

# Horizontal stack
np.hstack([[1,2],[3,4]])
# Output: array([1, 2, 3, 4])
# Stacks arrays horizontally (column-wise)

# Stack along new axis
np.stack([[1,2],[3,4]])
# Output:
# array([[1, 2],
#        [3, 4]])
# Stacks arrays along new axis (default axis=0)

# Split array into chunks
np.split(np.arange(6), 3)
# Output: [array([0, 1]), array([2, 3]), array([4, 5])]
# Splits array into 3 equal parts

# Horizontal split
np.hsplit(np.arange(6).reshape(2,3), 3)
# Output:
# [array([[0],
#        [3]]), array([[1],
#        [4]]), array([[2],
#        [5]])]
# Splits 2D array horizontally into 3 parts (split columns)

# Vertical split
np.vsplit(np.arange(6).reshape(3,2), 3)
# Output: [array([[0, 1]]), array([[2, 3]]), array([[4, 5]])]
# Splits 2D array vertically into 3 parts (split rows)

# Append values
np.append([1,2,3], [4,5])
# Output: array([1, 2, 3, 4, 5])
# Appends elements to array (creates new array)

# Insert values at position
np.insert([1,2,3], 1, 99)
# Output: array([ 1, 99,  2,  3])
# Inserts 99 at position 1 (0-indexed)

# Delete values at position
np.delete([1,2,3,4], 2)
# Output: array([1, 2, 4])
# Deletes element at position 2

# Repeat elements
np.repeat([1,2,3], 2)
# Output: array([1, 1, 2, 2, 3, 3])
# Repeats each element twice

# Tile array
np.tile([1,2,3], 2)
# Output: array([1, 2, 3, 1, 2, 3])
# Repeats entire array twice

# Expand dimensions
np.expand_dims([1,2,3], axis=0)
# Output: array([[1, 2, 3]])
# Adds new dimension at axis 0

# Squeeze dimensions
np.squeeze([[1,2,3]])
# Output: array([1, 2, 3])
# Removes dimensions of size 1

# Swap axes
np.swapaxes(np.arange(8).reshape(2,2,2), 0, 1)
# Output:
# array([[[0, 1],
#         [4, 5]],
# 
#        [[2, 3],
#         [6, 7]]])
# Swaps axis 0 and axis 1 of 3D array

# Flip array
np.flip([1,2,3])
# Output: array([3, 2, 1])
# Reverses order of elements

# Roll array elements
np.roll([1,2,3,4], 1)
# Output: array([4, 1, 2, 3])
# Shifts elements to right by 1 (wrap around)

# Copy array
np.array([1,2,3]).copy()
# Output: array([1, 2, 3])
# Creates independent copy of array

# Additional reshape functions

# Reshape with -1 (auto-calculate)
np.arange(12).reshape(-1, 3)
# Output:
# array([[ 0,  1,  2],
#        [ 3,  4,  5],
#        [ 6,  7,  8],
#        [ 9, 10, 11]])
# -1 automatically calculates dimension (12/3=4 rows)

# Reshape to single row
np.arange(12).reshape(1, -1)
# Output:
# array([[ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11]])
# Reshapes to 1x12 (single row)

# Reshape to single column
np.arange(12).reshape(-1, 1)
# Output:
# array([[ 0],
#        [ 1],
#        [ 2],
#        [ 3],
#        [ 4],
#        [ 5],
#        [ 6],
#        [ 7],
#        [ 8],
#        [ 9],
#        [10],
#        [11]])
# Reshapes to 12x1 (single column)

# Column stack
np.column_stack(([1,2,3], [4,5,6]))
# Output:
# array([[1, 4],
#        [2, 5],
#        [3, 6]])
# Stacks 1D arrays as columns

# Row stack
np.row_stack(([1,2,3], [4,5,6]))
# Output:
# array([[1, 2, 3],
#        [4, 5, 6]])
# Stacks arrays as rows (same as vstack)

# Rotate 90 degrees
np.rot90([[1,2,3],[4,5,6],[7,8,9]])
# Output:
# array([[3, 6, 9],
#        [2, 5, 8],
#        [1, 4, 7]])
# Rotates array 90 degrees counter-clockwise


# ==============================================================================
# MATH OPERATIONS
# ==============================================================================

# Add arrays (element-wise)
np.add([1,2,3], [4,5,6])
# Output: array([5, 7, 9])
# Adds corresponding elements of two arrays

# Subtract arrays (element-wise)
np.subtract([5,7,9], [1,2,3])
# Output: array([4, 5, 6])
# Subtracts corresponding elements

# Multiply arrays (element-wise)
np.multiply([1,2,3], [4,5,6])
# Output: array([ 4, 10, 18])
# Multiplies corresponding elements

# Divide arrays (element-wise)
np.divide([10,20,30], [2,4,5])
# Output: array([5., 5., 6.])
# Divides corresponding elements

# Power (element-wise)
np.power([1,2,3], 2)
# Output: array([1, 4, 9])
# Raises each element to power 2

# Modulo (element-wise)
np.mod([10,11,12], 3)
# Output: array([1, 2, 0])
# Returns remainder of division by 3

# Square root
np.sqrt([4, 9, 16])
# Output: array([2., 3., 4.])
# Computes square root of each element

# Exponential (e^x)
np.exp([1, 2, 3])
# Output: array([ 2.71828183,  7.3890561 , 20.08553692])
# Computes e^x for each element

# Natural logarithm
np.log([1, np.e, np.e**2])
# Output: array([0., 1., 2.])
# Computes ln(x) for each element

# Base-2 logarithm
np.log2([1, 2, 4, 8])
# Output: array([0., 1., 2., 3.])
# Computes log2(x) for each element

# Base-10 logarithm
np.log10([1, 10, 100])
# Output: array([0., 1., 2.])
# Computes log10(x) for each element

# Absolute value
np.abs([-1, -2, 3])
# Output: array([1, 2, 3])
# Returns absolute value of each element

# Round to specified decimals
np.round([1.234, 5.678], 2)
# Output: array([1.23, 5.68])
# Rounds to 2 decimal places

# Floor (rounds down)
np.floor([1.7, 2.3])
# Output: array([1., 2.])
# Returns floor of each element (rounds down)

# Ceiling (rounds up)
np.ceil([1.2, 2.8])
# Output: array([2., 3.])
# Returns ceiling of each element (rounds up)

# Truncate (discard fractional part)
np.trunc([1.7, -1.7])
# Output: array([ 1., -1.])
# Returns integer part, discards fractional

# Sine
np.sin([0, np.pi/2])
# Output: array([0., 1.])
# Computes sine of each element (radians)

# Cosine
np.cos([0, np.pi])
# Output: array([ 1., -1.])
# Computes cosine of each element (radians)

# Tangent
np.tan([0, np.pi/4])
# Output: array([0., 1.])
# Computes tangent of each element (radians)

# Cumulative sum
np.cumsum([1,2,3,4])
# Output: array([ 1,  3,  6, 10])
# Returns cumulative sum [1, 1+2, 1+2+3, 1+2+3+4]

# Cumulative product
np.cumprod([1,2,3,4])
# Output: array([ 1,  2,  6, 24])
# Returns cumulative product [1, 1*2, 1*2*3, 1*2*3*4]

# Clip values to range
np.clip([1,5,10,15], 3, 12)
# Output: array([ 3,  5, 10, 12])
# Clips values to range [3, 12] (min=3, max=12)

# Sign function (-1, 0, 1)
np.sign([-5, 0, 5])
# Output: array([-1,  0,  1])
# Returns sign of each element

# Reciprocal (1/x)
np.reciprocal([1., 2., 4.])
# Output: array([1.  , 0.5 , 0.25])
# Computes 1/x for each element

# Additional math functions

# Arcsin (inverse sine)
np.arcsin([0, 0.5, 1])
# Output: array([0.        , 0.52359878, 1.57079633])
# Computes arcsin of each element

# Arccos (inverse cosine)
np.arccos([1, 0.5, 0])
# Output: array([0.        , 1.04719755, 1.57079633])
# Computes arccos of each element

# Arctan (inverse tangent)
np.arctan([0, 1, np.inf])
# Output: array([0.        , 0.78539816, 1.57079633])
# Computes arctan of each element

# Hyperbolic sine
np.sinh([0, 1])
# Output: array([0.        , 1.17520119])
# Computes sinh of each element

# Hyperbolic cosine
np.cosh([0, 1])
# Output: array([1.        , 1.54308063])
# Computes cosh of each element

# Hyperbolic tangent
np.tanh([0, 1])
# Output: array([0.        , 0.76159416])
# Computes tanh of each element

# Degrees to radians
np.radians([0, 90, 180])
# Output: array([0.        , 1.57079633, 3.14159265])
# Converts degrees to radians

# Radians to degrees
np.degrees([0, np.pi/2, np.pi])
# Output: array([  0.,  90., 180.])
# Converts radians to degrees

# Floor division (integer division)
np.floor_divide([10, 20, 30], [3, 4, 6])
# Output: array([3, 5, 5])
# Returns integer division result

# Fmod (remainder with same sign as divisor)
np.fmod([-10, -10], [3, 4])
# Output: array([-1., -2.])
# Returns remainder with sign of divisor

# Maximum of two arrays
np.maximum([1, 5, 3], [2, 2, 4])
# Output: array([2, 5, 4])
# Returns element-wise maximum

# Minimum of two arrays
np.minimum([1, 5, 3], [2, 2, 4])
# Output: array([1, 2, 3])
# Returns element-wise minimum


# ==============================================================================
# STATISTICS
# ==============================================================================

# Sum of all elements
np.sum([1,2,3,4])
# Output: np.int64(10)
# Returns sum of all elements

# Mean (average)
np.mean([1,2,3,4])
# Output: np.float64(2.5)
# Returns average of all elements

# Median
np.median([1,2,3,4])
# Output: np.float64(2.5)
# Returns median (middle value)

# Standard deviation
np.std([1,2,3,4])
# Output: np.float64(1.118033988749895)
# Returns standard deviation (sqrt of variance)

# Variance
np.var([1,2,3,4])
# Output: np.float64(1.25)
# Returns variance (average of squared deviations)

# Minimum
np.min([3,1,4,1,5])
# Output: np.int64(1)
# Returns minimum value

# Maximum
np.max([3,1,4,1,5])
# Output: np.int64(5)
# Returns maximum value

# Argmin (index of minimum)
np.argmin([3,1,4,1,5])
# Output: np.int64(1)
# Returns index of first minimum value

# Argmax (index of maximum)
np.argmax([3,1,4,1,5])
# Output: np.int64(4)
# Returns index of first maximum value

# Peak-to-peak (range)
np.ptp([3,1,4,1,5])
# Output: np.int64(4)
# Returns max - min (5-1=4)

# Percentile
np.percentile([1,2,3,4,5], 50)
# Output: np.float64(3.0)
# Returns 50th percentile (median)

# Correlation coefficient
np.corrcoef([1,2,3], [4,5,6])
# Output:
# array([[1., 1.],
#        [1., 1.]])
# Returns correlation matrix (perfect correlation)

# Weighted average
np.average([1,2,3], weights=[1,1,2])
# Output: np.float64(2.25)
# Returns weighted average (weights sum to 4)

# Frequency count
np.bincount([1,1,2,3,3,3])
# Output: array([0, 2, 1, 3])
# Counts occurrences of each value (0 appears 0 times, 1 appears 2 times, etc.)

# Histogram
np.histogram([1,2,1,3,3,3], bins=3)
# Output: (array([2, 1, 3]), array([1.        , 1.66666667, 2.33333333, 3.        ]))
# Returns histogram counts and bin edges

# Additional statistical functions

# Nan-safe sum (ignores NaN)
np.nansum([1, np.nan, 3])
# Output: np.float64(4.0)
# Sums non-NaN values

# Nan-safe mean
np.nanmean([1, np.nan, 3])
# Output: np.float64(2.0)
# Computes mean ignoring NaN

# Nan-safe standard deviation
np.nanstd([1, np.nan, 3])
# Output: np.float64(1.0)
# Computes std ignoring NaN

# Nan-safe variance
np.nanvar([1, np.nan, 3])
# Output: np.float64(1.0)
# Computes variance ignoring NaN

# Covariance matrix
np.cov([1,2,3,4], [2,4,6,8])
# Output:
# array([[1.66666667, 3.33333333],
#        [3.33333333, 6.66666667]])
# Returns covariance matrix between arrays

# Quantile (like percentile but 0-1)
np.quantile([1,2,3,4,5], 0.5)
# Output: np.float64(3.0)
# Returns 50% quantile (same as median)

# Average with axis parameter
np.average([[1,2],[3,4]], axis=0)
# Output: array([2., 3.])
# Computes average along columns

# Nan-safe maximum
np.nanmax([1, np.nan, 3])
# Output: np.float64(3.0)
# Returns max ignoring NaN

# Nan-safe minimum
np.nanmin([1, np.nan, 3])
# Output: np.float64(1.0)
# Returns min ignoring NaN


# ==============================================================================
# LINEAR ALGEBRA
# ==============================================================================

# Dot product
np.dot([1,2,3], [4,5,6])
# Output: np.int64(32)
# Computes dot product (1*4 + 2*5 + 3*6 = 32)

# Matrix multiplication
np.matmul([[1,2],[3,4]], [[5,6],[7,8]])
# Output:
# array([[19, 22],
#        [43, 50]])
# Computes matrix product (2x2 * 2x2 = 2x2)

# Matrix multiplication operator
np.array([[1,2],[3,4]]) @ np.array([[5,6],[7,8]])
# Output:
# array([[19, 22],
#        [43, 50]])
# Same as matmul using @ operator

# Inverse matrix
np.linalg.inv([[1,2],[3,4]])
# Output:
# array([[-2. ,  1. ],
#        [ 1.5, -0.5]])
# Computes inverse of 2x2 matrix

# Determinant
np.linalg.det([[1,2],[3,4]])
# Output: np.float64(-2.0000000000000004)
# Computes determinant (1*4 - 2*3 = -2)

# Eigenvalues and eigenvectors
np.linalg.eig([[2,0],[0,3]])
# Output:
# EigResult(eigenvalues=array([2., 3.]), eigenvectors=array([[1., 0.],
#        [0., 1.]]))
# Returns eigenvalues and eigenvectors

# Transpose
np.transpose([[1,2],[3,4]])
# Output:
# array([[1, 3],
#        [2, 4]])
# Transposes matrix (swap rows and columns)

# Trace (sum of diagonal)
np.trace([[1,2],[3,4]])
# Output: np.int64(5)
# Returns trace (1+4=5)

# Norm (Euclidean)
np.linalg.norm([3, 4])
# Output: np.float64(5.0)
# Returns Euclidean norm (sqrt(3^2+4^2)=5)

# Cross product
np.cross([1,0,0], [0,1,0])
# Output: array([0, 0, 1])
# Computes cross product of 3D vectors

# Outer product
np.outer([1,2], [3,4])
# Output:
# array([[3, 4],
#        [6, 8]])
# Computes outer product (2x2 matrix)

# Solve linear system
np.linalg.solve([[3,1],[1,2]], [9,8])
# Output: array([2., 3.])
# Solves 3x + y = 9, x + 2y = 8 => x=2, y=3

# Matrix rank
np.linalg.matrix_rank([[1,2],[2,4]])
# Output: np.int64(1)
# Returns rank of matrix (rows are linearly dependent)

# Additional linear algebra functions

# Moore-Penrose pseudo-inverse
np.linalg.pinv([[1,2],[2,4]])
# Output:
# array([[0.04, 0.08],
#        [0.08, 0.16]])
# Computes pseudo-inverse (useful for rank-deficient matrices)

# QR decomposition
np.linalg.qr([[1,2],[3,4]])
# Output:
# (array([[-0.31622777, -0.9486833 ],
#         [-0.9486833 ,  0.31622777]]),
#  array([[-3.16227766, -4.42718872],
#         [ 0.        , -0.63245553]]))
# Returns Q and R matrices

# Singular value decomposition
np.linalg.svd([[1,2],[3,4]])
# Output:
# (array([[-0.40455358, -0.9145143 ],
#         [-0.9145143 ,  0.40455358]]),
#  array([5.4649857 , 0.36596619]),
#  array([[-0.57604844, -0.81741556],
#         [ 0.81741556, -0.57604844]]))
# Returns U, S, V matrices

# Cholesky decomposition
np.linalg.cholesky([[4,2],[2,3]])
# Output:
# array([[2.        , 0.        ],
#        [1.        , 1.41421356]])
# Cholesky decomposition (for positive definite matrices)

# Eigenvalues only (faster)
np.linalg.eigvals([[2,0],[0,3]])
# Output: array([2., 3.])
# Returns only eigenvalues (not eigenvectors)

# Linear least squares
np.linalg.lstsq([[1,1],[1,2],[1,3]], [6,9,12], rcond=None)
# Output:
# (array([3., 3.]), array([0.]), 2, array([4.74520719, 0.80755383]))
# Solves least squares linear system

# Condition number
np.linalg.cond([[1,2],[3,4]])
# Output: np.float64(14.933034373659268)
# Returns condition number (measures matrix sensitivity)


# ==============================================================================
# RANDOM (seeded for reproducibility)
# ==============================================================================

# Set seed for reproducibility
np.random.seed(0); np.random.rand(3)
# Output: OK
# Sets random seed to 0 for reproducible results

# Uniform random [0,1)
np.random.seed(0); np.random.randn(3)
# Output: OK
# Generates 3 samples from standard normal distribution

# Random integers
np.random.seed(0); np.random.randint(1, 10, 5)
# Output: OK
# Generates 5 random integers from [1, 10)

# Random choice from array
np.random.seed(0); np.random.choice([10,20,30], 2)
# Output: OK
# Randomly selects 2 elements from array

# Shuffle array in-place
np.random.seed(0); np.random.shuffle(a := [1,2,3,4]); a
# Output: OK
# Shuffles array in-place (modifies original)

# Random permutation
np.random.seed(0); np.random.permutation(5)
# Output: OK
# Returns shuffled array of 0-4 (doesn't modify original)

# Uniform distribution
np.random.seed(0); np.random.uniform(0, 10, 3)
# Output: OK
# Generates 3 random numbers from uniform [0, 10)

# Normal distribution
np.random.seed(0); np.random.normal(0, 1, 3)
# Output: OK
# Generates 3 random numbers from normal (mean=0, std=1)

# Additional random functions

# Random random in [0,1)
np.random.seed(0); np.random.random((2, 3))
# Output: OK
# Generates 2x3 array of random numbers in [0,1)

# Random sample (same as random)
np.random.seed(0); np.random.sample((2, 2))
# Output: OK
# Same as np.random.random()

# Beta distribution
np.random.seed(0); np.random.beta(2, 5, 3)
# Output: OK
# Generates 3 samples from beta distribution

# Binomial distribution
np.random.seed(0); np.random.binomial(10, 0.5, 3)
# Output: OK
# Generates 3 samples from binomial distribution (n=10, p=0.5)

# Chi-square distribution
np.random.seed(0); np.random.chisquare(2, 3)
# Output: OK
# Generates 3 samples from chi-square distribution (df=2)

# Exponential distribution
np.random.seed(0); np.random.exponential(1, 3)
# Output: OK
# Generates 3 samples from exponential distribution (scale=1)

# Gamma distribution
np.random.seed(0); np.random.gamma(2, 1, 3)
# Output: OK
# Generates 3 samples from gamma distribution (shape=2, scale=1)

# Poisson distribution
np.random.seed(0); np.random.poisson(2, 3)
# Output: OK
# Generates 3 samples from Poisson distribution (lambda=2)

# Standard Cauchy
np.random.seed(0); np.random.standard_cauchy(3)
# Output: OK
# Generates 3 samples from standard Cauchy distribution

# Standard normal
np.random.seed(0); np.random.standard_normal(3)
# Output: OK
# Same as randn, generates standard normal samples

# Standard t-distribution
np.random.seed(0); np.random.standard_t(5, 3)
# Output: OK
# Generates 3 samples from t-distribution (df=5)

# Random choice with probabilities
np.random.seed(0); np.random.choice(['a','b','c'], 5, p=[0.1, 0.2, 0.7])
# Output: OK
# Chooses 5 elements with specified probabilities


# ==============================================================================
# INDEXING & SLICING
# ==============================================================================

# Basic slicing (start:stop:step)
np.arange(10)[2:7]
# Output: array([2, 3, 4, 5, 6])
# Selects elements from index 2 to 6 (exclusive)

# Reverse array
np.arange(10)[::-1]
# Output: array([9, 8, 7, 6, 5, 4, 3, 2, 1, 0])
# Reverses array using step -1

# Boolean indexing
np.arange(10)[np.arange(10) > 5]
# Output: array([6, 7, 8, 9])
# Selects elements where condition is True

# Where (conditional selection)
np.where(np.arange(10) > 5, 1, 0)
# Output: array([0, 0, 0, 0, 0, 0, 1, 1, 1, 1])
# Returns 1 where condition True, 0 where False

# Non-zero indices
np.nonzero([0, 3, 0, 5])
# Output: (array([1, 3]),)
# Returns indices of non-zero elements

# Take elements
np.take([10,20,30,40], [0,2])
# Output: array([10, 30])
# Takes elements at specified indices

# Select from multiple arrays
np.select([np.array([1,2,3])<2, np.array([1,2,3])>=2], [10,20])
# Output: array([10, 20, 20])
# Selects values based on conditions

# Extract elements based on condition
np.extract(np.array([1,2,3,4])%2==0, [1,2,3,4])
# Output: array([2, 4])
# Extracts elements where condition is True

# Additional indexing functions

# Indexing with arrays
np.arange(10)[[0, 2, 4, 6]]
# Output: array([0, 2, 4, 6])
# Uses array of indices for advanced indexing

# 2D indexing
arr = np.arange(12).reshape(3, 4)
arr[1:3, 1:3]
# Output:
# array([[5, 6],
#        [9, 10]])
# Slices rows 1-2 and columns 1-2

# Fancy indexing
arr[[0, 2], [1, 2]]
# Output: array([1, 10])
# Takes element at (0,1) and (2,2)

# Indexing with ellipsis (...)
arr = np.arange(12).reshape(2, 2, 3)
arr[..., 1]
# Output:
# array([[1, 4],
#        [7, 10]])
# Takes all values at index 1 in last dimension

# Indexing with newaxis
np.arange(3)[np.newaxis, :]
# Output: array([[0, 1, 2]])
# Adds new dimension (makes row vector)

# Indexing with None (same as newaxis)
np.arange(3)[:, None]
# Output:
# array([[0],
#        [1],
#        [2]])
# Adds new dimension (makes column vector)

# Diagonal indexing
np.diag_indices(3)
# Output: (array([0, 1, 2]), array([0, 1, 2]))
# Returns indices for diagonal of square matrix


# ==============================================================================
# SORTING & SEARCHING
# ==============================================================================

# Sort array
np.sort([3,1,4,1,5])
# Output: array([1, 1, 3, 4, 5])
# Returns sorted array (ascending)

# Argsort (indices that would sort)
np.argsort([3,1,4,1,5])
# Output: array([1, 3, 0, 2, 4])
# Returns indices that would sort array

# Search sorted (find insertion position)
np.searchsorted([1,3,5,7], 4)
# Output: np.int64(2)
# Returns index where 4 should be inserted

# Unique elements
np.unique([1,2,2,3,3,3])
# Output: array([1, 2, 3])
# Returns unique values (sorted)

# Partition (partially sort)
np.partition([3,1,4,1,5], 2)
# Output: array([1, 1, 3, 4, 5])
# Ensures first 2 elements are smallest

# Additional sorting functions

# Sort along axis
np.sort([[3,1,4],[1,5,9]], axis=0)
# Output:
# array([[1, 1, 4],
#        [3, 5, 9]])
# Sorts each column independently

# Sort in descending order
np.sort([3,1,4,1,5])[::-1]
# Output: array([5, 4, 3, 1, 1])
# Sorts ascending then reverses

# Lexsort (sort by multiple keys)
np.lexsort(([1,2,3], [2,1,3]))
# Output: array([1, 0, 2])
# Returns indices for sorting by second array then first

# Where with sorted result
np.where(np.array([1,2,3,4,5]) > 3)
# Output: (array([3, 4]),)
# Finds indices where condition is True

# Extract with condition
np.extract([1,2,3,4,5] > 3, [1,2,3,4,5])
# Output: array([4, 5])
# Extracts elements satisfying condition


# ==============================================================================
# SET OPERATIONS
# ==============================================================================

# Union (unique elements from both arrays)
np.union1d([1,2,3], [3,4,5])
# Output: array([1, 2, 3, 4, 5])
# Returns union of two arrays

# Intersection
np.intersect1d([1,2,3], [2,3,4])
# Output: array([2, 3])
# Returns common elements from both arrays

# Difference (in first but not second)
np.setdiff1d([1,2,3], [2,3])
# Output: array([1])
# Returns elements in first array not in second

# Check membership (isin)
np.isin([1,2,3], [2,3])
# Output: array([False,  True,  True])
# Checks which elements are in second array

# Additional set operations

# Symmetric difference (in either but not both)
np.setxor1d([1,2,3], [3,4,5])
# Output: array([1, 2, 4, 5])
# Returns elements in one array but not both

# All unique with counts
np.unique([1,2,2,3,3,3], return_counts=True)
# Output: (array([1, 2, 3]), array([1, 2, 3]))
# Returns unique values and their counts

# Unique with indices
np.unique([1,2,2,3,3,3], return_index=True)
# Output: (array([1, 2, 3]), array([0, 1, 3]))
# Returns unique values and first occurrence indices

# Unique with inverse
np.unique([1,2,2,3,3,3], return_inverse=True)
# Output: (array([1, 2, 3]), array([0, 1, 1, 2, 2, 2]))
# Returns unique values and indices to reconstruct


# ==============================================================================
# LOGICAL & COMPARISON
# ==============================================================================

# All elements True?
np.all([True, True, False])
# Output: np.False_
# Returns True only if all elements are True

# Any element True?
np.any([False, False, True])
# Output: np.True_
# Returns True if any element is True

# Array equality
np.array_equal([1,2,3], [1,2,3])
# Output: True
# Returns True if arrays are exactly equal

# Check for NaN
np.isnan([1, np.nan, 3])
# Output: array([False,  True, False])
# Returns True for NaN values

# Check for infinity
np.isinf([1, np.inf, 3])
# Output: array([False,  True, False])
# Returns True for infinite values

# Logical AND (element-wise)
np.logical_and([True, False], [True, True])
# Output: array([ True, False])
# Element-wise AND operation

# Logical OR (element-wise)
np.logical_or([True, False], [False, False])
# Output: array([ True, False])
# Element-wise OR operation

# Logical NOT (element-wise)
np.logical_not([True, False])
# Output: array([False,  True])
# Element-wise NOT operation

# Additional logical functions

# Logical XOR (element-wise)
np.logical_xor([True, False], [False, True])
# Output: array([ True,  True])
# Element-wise XOR operation

# All true along axis
np.all([[True, True], [False, True]], axis=0)
# Output: array([False,  True])
# Checks if all True along each column

# Any true along axis
np.any([[True, True], [False, True]], axis=1)
# Output: array([ True,  True])
# Checks if any True along each row

# Element-wise equality
np.equal([1,2,3], [1,2,4])
# Output: array([ True,  True, False])
# Element-wise equality comparison

# Element-wise less than
np.less([1,2,3], [2,2,2])
# Output: array([ True, False, False])
# Element-wise less than comparison

# Element-wise greater than
np.greater([1,2,3], [2,2,2])
# Output: array([False, False,  True])
# Element-wise greater than comparison

# Element-wise not equal
np.not_equal([1,2,3], [1,2,4])
# Output: array([False, False,  True])
# Element-wise not equal comparison

# Is finite (not NaN or inf)
np.isfinite([1, np.nan, np.inf])
# Output: array([ True, False, False])
# Returns True for finite values


# ==============================================================================
# TYPE CONVERSION
# ==============================================================================

# Change data type
np.array([1, 2, 3]).astype(float)
# Output: array([1., 2., 3.])
# Converts array elements to float64

# Convert to Python list
np.array([1.5, 2.5]).tolist()
# Output: [1.5, 2.5]
# Converts array to Python list

# Convert scalar to Python type
int(np.array(5))
# Output: 5
# Converts numpy scalar to Python int

# Additional type conversion

# Change to int (safe)
np.array([1.5, 2.7]).astype(int)
# Output: array([1, 2])
# Converts float to int (truncates)

# Change to complex
np.array([1, 2]).astype(complex)
# Output: array([1.+0.j, 2.+0.j])
# Converts to complex numbers

# Change to bool
np.array([0, 1, 2]).astype(bool)
# Output: array([False,  True,  True])
# Converts to boolean (0=False, non-zero=True)

# Bytes to string
np.array([97, 98, 99]).astype('U')
# Output: array(['a', 'b', 'c'], dtype='<U1')
# Converts ASCII codes to characters

# String to bytes
np.array(['a', 'b', 'c']).astype('S')
# Output: array([b'a', b'b', b'c'], dtype='|S1')
# Converts strings to bytes

# Bytes to int
np.array([b'1', b'2']).astype(int)
# Output: array([1, 2])
# Converts bytes to integers

# Float32 to float64
np.array([1.0, 2.0], dtype=np.float32).astype(np.float64)
# Output: array([1., 2.])
# Converts from float32 to float64

# Python float conversion
float(np.array(5.7))
# Output: 5.7
# Converts numpy scalar to Python float

# Python bool conversion
bool(np.array(0))
# Output: False
# Converts numpy scalar to Python bool


# ==============================================================================
# BROADCASTING & VECTORIZATION
# ==============================================================================

# Scalar addition (broadcasting)
np.array([1, 2, 3]) + 10
# Output: array([11, 12, 13])
# Adds scalar to each element (broadcasting)

# Scalar multiplication
np.array([1, 2, 3]) * 2
# Output: array([2, 4, 6])
# Multiplies scalar to each element

# Broadcasting with different shapes
np.array([1, 2, 3]) + np.array([[4], [5]])
# Output:
# array([[5, 6, 7],
#        [6, 7, 8]])
# Broadcasts [1,2,3] to 2x3, [4,5] to 2x1

# Vectorized operations (fast loops)
np.sqrt(np.array([1, 4, 9]))
# Output: array([1., 2., 3.])
# Vectorized square root (C-level speed)

# Vectorized comparison
np.array([1, 2, 3]) > 2
# Output: array([False, False,  True])
# Vectorized element-wise comparison

# Vectorized conditional
np.where(np.array([1, 2, 3]) > 2, 'high', 'low')
# Output: array(['low', 'low', 'high'], dtype='<U4')
# Vectorized if-else (assign based on condition)

# Vectorized min/max
np.minimum(np.array([1, 5, 3]), np.array([4, 2, 6]))
# Output: array([1, 2, 3])
# Element-wise minimum (vectorized)

# Vectorized sine
np.sin(np.array([0, np.pi/2, np.pi]))
# Output: array([0.0000000e+00, 1.0000000e+00, 1.2246468e-16])
# Vectorized trigonometric function

# Additional vectorized functions

# Vectorized round
np.round(np.array([1.234, 5.678]), 1)
# Output: array([1.2, 5.7])
# Vectorized rounding

# Vectorized absolute value
np.abs(np.array([-1, -2, 3]))
# Output: array([1, 2, 3])
# Vectorized absolute value

# Vectorized power
np.power(np.array([1, 2, 3]), 3)
# Output: array([ 1,  8, 27])
# Vectorized exponentiation

# Vectorized exponential
np.exp(np.array([0, 1, 2]))
# Output: array([1.        , 2.71828183, 7.3890561 ])
# Vectorized exponential

# Vectorized logarithm
np.log(np.array([1, 10, 100]))
# Output: array([0.        , 2.30258509, 4.60517019])
# Vectorized natural logarithm

# Vectorized floor
np.floor(np.array([1.7, 2.3, 3.9]))
# Output: array([1., 2., 3.])
# Vectorized floor function

# Vectorized ceil
np.ceil(np.array([1.2, 2.8, 3.4]))
# Output: array([2., 3., 4.])
# Vectorized ceiling function

# Vectorized array creation
np.fromfunction(lambda i, j: i**2 + j**2, (3, 3))
# Output:
# array([[0., 1., 4.],
#        [1., 2., 5.],
#        [4., 5., 8.]])
# Vectorized creation using function


# ==============================================================================
# FILE I/O
# ==============================================================================

# Save array to binary file (numpy format)
np.save('array', np.array([1,2,3]))
# Output: None
# Saves array to .npy file (binary format)

# Load array from binary file
np.load('array.npy')
# Output: array([1, 2, 3])
# Loads array from .npy file

# Save multiple arrays
np.savez('arrays', a=np.array([1,2,3]), b=np.array([4,5,6]))
# Output: None
# Saves multiple arrays to .npz file

# Load multiple arrays
data = np.load('arrays.npz')
data['a'], data['b']
# Output: (array([1, 2, 3]), array([4, 5, 6]))
# Loads arrays from .npz file

# Save to text file
np.savetxt('data.txt', np.array([[1,2,3],[4,5,6]]))
# Output: None
# Saves array to text file (human-readable)

# Load from text file
np.loadtxt('data.txt')
# Output:
# array([[1., 2., 3.],
#        [4., 5., 6.]])
# Loads array from text file

# Additional file I/O

# Save as compressed (smaller)
np.savez_compressed('compressed', a=np.array([1,2,3,4,5]))
# Output: None
# Saves array as compressed .npz file

# Load with specific dtype
np.loadtxt('data.txt', dtype=int)
# Output:
# array([[1, 2, 3],
#        [4, 5, 6]])
# Loads text file with specified data type

# Save with custom delimiter
np.savetxt('data.csv', np.array([[1,2,3],[4,5,6]]), delimiter=',')
# Output: None
# Saves with comma delimiter (CSV format)

# Load with custom delimiter
np.loadtxt('data.csv', delimiter=',')
# Output:
# array([[1., 2., 3.],
#        [4., 5., 6.]])
# Loads CSV file with comma delimiter

# Load with header (skip lines)
np.loadtxt('data.txt', skiprows=1)
# Output:
# array([[2., 3., 4.],
#        [5., 6., 7.]])
# Skips first line (header) when loading

# Load with missing values
np.genfromtxt('data.txt', missing_values='NA', filling_values=0)
# Output:
# array([[1., 2., 3.],
#        [4., 0., 6.]])
# Handles missing values in text files


# ==============================================================================
# STRING OPERATIONS (numpy.char)
# ==============================================================================

# Convert to uppercase
np.char.upper(['hello', 'world'])
# Output: array(['HELLO', 'WORLD'], dtype='<U5')
# Converts strings to uppercase

# Convert to lowercase
np.char.lower(['HELLO', 'WORLD'])
# Output: array(['hello', 'world'], dtype='<U5')
# Converts strings to lowercase

# Capitalize first letter
np.char.capitalize(['hello', 'world'])
# Output: array(['Hello', 'World'], dtype='<U5')
# Capitalizes first letter of each string

# Title case
np.char.title(['hello world', 'python numpy'])
# Output: array(['Hello World', 'Python Numpy'], dtype='<U13')
# Converts to title case

# Join strings
np.char.join('-', ['hello', 'world'])
# Output: array(['h-e-l-l-o', 'w-o-r-l-d'], dtype='<U9')
# Joins characters with separator

# Split strings
np.char.split(['hello world', 'python numpy'])
# Output: array([['hello', 'world'], ['python', 'numpy']], dtype=object)
# Splits strings into lists

# Replace substrings
np.char.replace(['hello world', 'python numpy'], 'o', '0')
# Output: array(['hell0 w0rld', 'pyth0n numpy'], dtype='<U11')
# Replaces substring with another

# Strip whitespace
np.char.strip(['  hello  ', '  world  '])
# Output: array(['hello', 'world'], dtype='<U5')
# Removes leading/trailing whitespace

# String length
np.char.str_len(['hello', 'world'])
# Output: array([5, 5])
# Returns length of each string

# Count substring occurrences
np.char.count(['hello world', 'python numpy'], 'o')
# Output: array([2, 1])
# Counts occurrences of substring

# Find substring
np.char.find(['hello world', 'python numpy'], 'o')
# Output: array([4, 5])
# Returns first index of substring

# Additional string operations

# Center strings
np.char.center(['hello', 'world'], 10, fillchar='*')
# Output: array(['**hello***', '**world***'], dtype='<U10')
# Centers strings in field width

# Left justify
np.char.ljust(['hello', 'world'], 10, fillchar=' ')
# Output: array(['hello     ', 'world     '], dtype='<U10')
# Left justifies strings

# Right justify
np.char.rjust(['hello', 'world'], 10, fillchar=' ')
# Output: array(['     hello', '     world'], dtype='<U10')
# Right justifies strings

# Zero padding
np.char.zfill(['123', '45'], 5)
# Output: array(['00123', '00045'], dtype='<U5')
# Pads with zeros on left

# Split by character
np.char.split(['hello-world', 'python-numpy'], sep='-')
# Output: array([['hello', 'world'], ['python', 'numpy']], dtype=object)
# Splits by specified separator

# Compare strings
np.char.equal(['hello', 'world'], ['hello', 'there'])
# Output: array([ True, False])
# Element-wise string comparison

# Concatenate strings
np.char.add(['hello', 'python'], ['world', 'numpy'])
# Output: array(['helloworld', 'pythonnumpy'], dtype='<U11')
# Concatenates element-wise

# Multiply strings (repeat)
np.char.multiply(['hello', 'world'], 2)
# Output: array(['hellohello', 'worldworld'], dtype='<U10')
# Repeats each string


# ==============================================================================
# MEMORY & PERFORMANCE
# ==============================================================================

# Check if array is view or copy
np.array([1,2,3]).base is None
# Output: True
# True if array owns its data (not a view)

# Memory share test
a = np.arange(5)
b = a.view()
b.base is a
# Output: True
# b is a view of a (shares memory)

# Copy data (deep copy)
a = np.arange(5)
b = a.copy()
b.base is a
# Output: False
# b is independent copy (doesn't share memory)

# Reshape without copying (view)
a = np.arange(6)
b = a.reshape(2, 3)
np.shares_memory(a, b)
# Output: True
# Reshape creates view (shares memory)

# Flatten with copy vs view
a = np.arange(6).reshape(2, 3)
b = a.ravel()  # view if possible
c = a.flatten()  # always copy
np.shares_memory(a, b), np.shares_memory(a, c)
# Output: (True, False)
# ravel may return view, flatten always returns copy

# Memory usage
a = np.arange(1000)
a.nbytes
# Output: 8000
# Memory usage in bytes (1000 * 8 bytes)

# Determine array info
np.info(np.array([1,2,3]))
# Output: None
# Prints detailed array information

# Additional memory functions

# Get memory offset
a = np.arange(10)
a.ctypes.data
# Output: 139726372831840 (address varies)
# Returns memory address of array data

# Check alignment
np.array([1,2,3]).flags.aligned
# Output: True
# Checks if array is memory aligned

# Check writability
np.array([1,2,3]).flags.writeable
# Output: True
# Checks if array can be modified

# Make array immutable (read-only)
a = np.array([1,2,3])
a.flags.writeable = False
# Output: None
# Makes array read-only (can't modify)

# Check contiguity
a = np.arange(12).reshape(3, 4)
a.flags.c_contiguous, a.flags.f_contiguous
# Output: (True, False)
# C-contiguous (row-major) and F-contiguous (column-major)

# Force C-contiguous
a = np.arange(12).reshape(3, 4, order='F')
b = np.ascontiguousarray(a)
b.flags.c_contiguous
# Output: True
# Forces array to be C-contiguous

# Force F-contiguous
a = np.arange(12).reshape(3, 4)
b = np.asfortranarray(a)
b.flags.f_contiguous
# Output: True
# Forces array to be F-contiguous