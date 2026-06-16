# rotate whole array

# arr = [1, 2, 3, 4, 5]
# print(arr[-1:0:-1] + arr[:1])

# # rotate part of array
# arr = [1, 2, 3, 4, 5]
# k = 2
# print(arr[-k:] + arr[:-k])

# rotate part of array in place
arr = [1, 2, 3, 4, 5]
k = 2
arr = arr[-k:] + arr[:-k]
print(arr)

