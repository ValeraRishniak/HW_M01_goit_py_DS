import numpy as np

# T1
a = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], dtype=int)
print(a)

# T2
m = np.array([[0, 0, 0], [0, 0, 0], [0, 0, 0]], dtype=int)
print(m)

# T3
m = np.random.randint(1, 11, size=(5, 5), dtype=int)
print(m)

# T4
m = np.random.rand(4, 4)
print(m)

# T5
m1 = np.random.randint(1, 11, size=(1, 5), dtype=int)
print(m1)
m2 = np.random.randint(1, 11, size=(1, 5), dtype=int)
print(m2)
sum_m1_m2 = m1 + m2
print(sum_m1_m2)
sub_m1_m2 = m1 - m2
print(sub_m1_m2)
mult_m1_m2 = m1 * m2
print(mult_m1_m2)

# T6
m1 = np.random.randint(1, 21, size=(7), dtype=int)
print(m1)
m2 = np.random.randint(1, 21, size=(7), dtype=int)
print(m2)
scalar_product = np.dot(m1, m2)
print(scalar_product)

# T7
m1 = np.random.randint(1, 11, size=(2,2), dtype=int)
print(m1)
m2 = np.random.randint(1, 11, size=(2,3), dtype=int)
print(m2)
matrix_mult = np.dot(m1, m2)
print(matrix_mult)


# T8
m1 = np.random.randint(1, 11, size=(3, 3), dtype=int)
print(m1)
inv_m1 = np.linalg.inv(m1)
print(inv_m1)


# T9
m1 = np.random.rand(4, 4)
print(m1)
transpos_m1 = m1.T
print(transpos_m1)


# T10
m1 = np.random.randint(1, 11, size=(3,4), dtype=int)
print("m1=", m1)
v1 = np.random.randint(1, 11, size=(4), dtype=int)
print("v1=", v1)
mul_m1_v1 = m1 * v1
print("mul", mul_m1_v1)
dot_m1_v1 = np.dot(m1, v1)
print("dot", dot_m1_v1)

# T11
m1 = np.random.rand(2,3)
print("m1=", m1)
v1 = np.random.rand(3)
print("v1=", v1)
mul_m1_v1 = m1 * v1
print("mul", mul_m1_v1)
dot_m1_v1 = np.dot(m1, v1)
print("dot", dot_m1_v1)

# T12
m1 = np.random.randint(1, 11, size=(2,2), dtype=int)
print("m1=", m1)
m2 = np.random.randint(1, 11, size=(2,2), dtype=int)
print("m2=", m2)
mul_m1_m2 = m1 * m2
print("mul", mul_m1_m2)
multiply_m1_m2 = np.multiply(m1, m2)
print("multiply", multiply_m1_m2)

# T13
m1 = np.random.randint(1, 11, size=(2,2), dtype=int)
print("m1=", m1)
m2 = np.random.randint(1, 11, size=(2,2), dtype=int)
print("m2=", m2)
dot_m1_m2 = np.dot(m1, m2)
print("dot", dot_m1_m2)

# T14
m1 = np.random.randint(1, 101, size=(5, 5), dtype=int)
print("m1=", m1)
sum_m1 = np.sum(m1)
print("sum", sum_m1)

# T15
m1 = np.random.randint(1, 11, size=(4, 4), dtype=int)
print("m1=", m1)
m2 = np.random.randint(1, 11, size=(4, 4), dtype=int)
print("m2=", m2)
diff_m1_m2 = m1 - m2
print("diff", diff_m1_m2)

# T16
m1 = np.random.rand(3, 3)
print("m1=", m1)
rows_sum = m1.sum(axis=1).reshape(-1, 1)
print("row_sums=", rows_sum)

# T17
m1 = np.random.randint(1, 11, size=(3,4), dtype=int)
print("m1=", m1)
exp_m = np.power(m1,2)
print("exp_m=", exp_m)

# T18
v1 = np.random.randint(1, 51, size=(4), dtype=int)
print("v1=", v1)
sqrt_v1 = np.sqrt(v1)
print("sqrt_v1=", sqrt_v1)
