import numpy as np  

a1 = np.array([1,2,3,4], dtype="uint32")
a2 = np.array([1,2,3,4.0])
b = np.array([[1,2,3,4],[5,6,7,8]])
print(b.size, b.shape, b.dtype, b[1,2], sep=", ")
# two's complement representation is widely used in computers for representing signed integers due to its simplicity and efficiency in arithmetic operations.


a = np.zeros((3,4), dtype="uint32")
a[1,2] = 66

b = 11*np.ones((3,1))


a = np.arange(12).reshape((3,4))
a[1], a[1, :]