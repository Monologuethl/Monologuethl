import numpy as np

arr = np.arange(12)
print('array is:', arr)

slice_one = arr[:4]
print('slice begins at 0 and ends at 4 is:', slice_one)

slice_two = arr[7:10]
print('slice begins at 7 and ends at 10 is:', slice_two)

slice_three = arr[0:12:4]
print('slice begins at 0 and ends at 12 with step 4 is:', slice_three)

arr = np.arange(12).reshape((3, 4))
print('array is:')
print(arr)

# 取第一维的索引 1 到索引 2 之间的元素，也就是第二行
# 取第二维的索引 1 到索引 3 之间的元素，也就是第二列和第三列
slice_one = arr[1:2, 1:3]
print('first slice is:')
print(slice_one)

# 取第一维的全部
# 按步长为 2 取第二维的索引 0 到末尾 之间的元素，也就是第一列和第三列
slice_two = arr[:, ::2]
print('second slice is:')
print(slice_two)

arr = np.arange(24).reshape((2, 3, 4))

print(arr)
print(arr[1, ...])  # 等价于 arr[1, :, :]
print(arr[..., 1])  # 等价于 arr[:, :, 1]

arr = np.array([
    [1, 2, 3, 4],
    [2, 4, 6, 8],
    [3, 6, 9, 12],
    [4, 8, 12, 16]
])
print('第二行第二列的值:', arr[1, 1])

arr = np.array([
    [1, 2, 3, 4],
    [2, 4, 6, 8],
    [3, 6, 9, 12],
    [4, 8, 12, 16]
])

print(arr[[0, 2], [3, 1]])

arr = np.array([[1, 2, 3, 4],
                [2, 4, 6, 8],
                [3, 6, 9, 12],
                [4, 8, 12, 16]])
mask = arr > 5

print('boolean mask is:')
print(mask)
print(arr[mask])

# 除了比较运算能产生 boolean mask 数组以外， Numpy 本身也提供了一些工具方法:
# numpy.iscomplex
# numpy.isreal
# numpy.isfinite
# numpy.isinf
# numpy.isnan
