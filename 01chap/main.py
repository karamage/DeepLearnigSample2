import numpy as np

x = np.array([1,2,3])
print(x.__class__)

print(x.shape)
print(x.ndim)

W = np.array([[1,2,3], [4,5,6]])
print(W.shape)
print(W.ndim)

W = np.array([[1,2,3], [4,5,6]])
X = np.array([[0,1,2], [3,4,5]])

print(W + X)
print(W * X)

# ベクトルの内積
a = np.array([1,2,3])
b = np.array([4,5,6])
print(np.dot(a, b))

# 行列の積
A = np.array([[1,2], [3,4]])
B = np.array([[5,6], [7,8]])
print(np.dot(A, B))

