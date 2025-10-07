# def min_max(nums):
#     if not nums:
#         return ("Value Error")
#     else:
#         mini = min(nums)
#         maxi = max(nums)
#         return (mini, maxi)
# print(min_max([3, -1, 5, 5, 0]))
# print(min_max([42]))
# print(min_max([-5, -2, -9]))
# print(min_max([1.5,2,2.0,-3.1]))
# print(min_max([]))




# def unique_sorted(numbers):
#     return (list(sorted(set(numbers))))
# print(unique_sorted([3, 1, 2, 1, 3]))
# print(unique_sorted([]))
# print(unique_sorted([-1, -1, 0, 2, 2]))
# print(unique_sorted([1.0, 1, 2.5, 2.5, 0]))



def flatten(mat):
    flat_list = []
    for row in mat:
        if isinstance(row, (list, tuple)):
            flat_list.extend(row)
        else:
            return("TypeError")
    return (flat_list)
print(flatten([[1, 2], [3, 4]]))
print(flatten([[1, 2], (3, 4, 5)]))
print(flatten([[1], [],[2, 3]]))
print(flatten([[1, 2], "ab"]))