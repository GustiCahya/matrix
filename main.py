import numpy as numpy
import numpy.linalg as m

A = numpy.array([[2,-1,1],[1,-3,6],[6,-1,-2]])
print("A =", A)
print("det(A) = ", m.det(A))
B= numpy.identity(3)
print("B =", B)
#reduksi baris
for i in range(0, len(B)):
    B[0][i]=A[0][i]-A[2][i]
    B[1][i]=A[1][i]-3*A[2][i]
    B[2][i]=A[2][i]*(-1/2)
print("setelah reduksi")
print(B)
print(m.det(B))
print(m.det(A))
