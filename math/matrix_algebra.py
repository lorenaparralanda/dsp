# Matrix Algebra

import numpy
from numpy import matrix
from numpy import linalg

A = matrix( [[1,2,3],[2,7,4]])
B = matrix( [[1,-1],[0,1]])
C = matrix( [[5,-1],[9,1],[6,0]])
D = matrix( [[3,-2,-1],[1,2,3]])
u = matrix( [[6,2,-3,5]])
v = matrix( [[3,5,-1,4]])
w = matrix( [[1],[8],[0],[5]]) 


# Matrix Dimensions

print A.shape 
# (2L, 3L)
print B.shape 
# (2L, 2L)
print C.shape 
# (3L, 2L)
print D.shape 
# (2L, 3L)
print u.shape 
# (1L, 4L)
print w.shape 
# (4L, 1L)


# Vector Operations

print u + v 
# [[ 9  7 -4  9]]
print u - v 
# [[ 3 -3 -2  1]]
x = 6
print u * v 
# [[ 36  12 -18  30]]
print x * u 
# not defined
print numpy.linalg.norm(u) 
# 8.60232526704


# Matrix Operations

print A + C 
# not defined
print A - C.T
# [[-4 -7 -3],[ 3  6  4]]
print C.T + 3*D
# [[14  3  3],[ 2  7  9]]
print B * A
# [[-1 -5 -1], [ 2  7  4]]
print B * A.T
# not defined


# Optional

print B * C 
# not defined
print C * B
# [[ 5 -6],[ 9 -8],[ 6 -6]]
print B**4
# [[ 1 -4],[ 0  1]]
print A * A.T
# [[14 28],[28 69]]
print D.T * D
# [[10 -4  0],[-4  8  8],[ 0  8 10]]
