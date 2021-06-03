'''
Optimal Approch Without maintaining the relative order
--------------
Time - O(N)
Space - O(1)
'''

# def moveElementToEnd(nums, target):
#     left = 0
#     right = len(nums) - 1

#     while left < right:
#         while nums[right] == target and left < right:
#             right -= 1
#         if nums[left] == target:
#             nums[left], nums[right] = nums[right], nums[left]
#             left += 1
#             right -= 1
#         else:
#             left += 1

#     return nums


'''
Optimal Approch While maintaining the relative order
--------------
Time - O(N)
Space - O(1)
'''


def moveElementToEnd(nums, target):
    i = 0

    for j in range(len(nums)):
        if nums[j] != target:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1

    return nums


nums = [2, 1, 2, 2, 2, 3, 4, 2]
target = 2
print(moveElementToEnd(nums, target))


nums = [0, 0, 0, 2, 2, 0, 0, 0]
target = 0
print(moveElementToEnd(nums, target))
