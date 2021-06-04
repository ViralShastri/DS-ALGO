'''
Linear Approch
--------------
Time - O(N)
Space - O(N)
'''


# def firstDuplicateValue(nums):
#     hashTable = {}
#     for num in nums:
#         if num in hashTable:
#             return num
#         hashTable[num] = 1
#     return -1


'''
Optimal Approch
--------------
Time - O(N)
Space - O(1)
'''


def firstDuplicateValue(nums):
    for num in nums:
        if nums[abs(num) - 1] < 0:
            return abs(num)
        nums[abs(num) - 1] *= -1
    return -1


nums = [2, 1, 5, 2, 3, 3, 4]
print(firstDuplicateValue(nums))

nums = [2, 1, 5, 3, 3, 2]
print(firstDuplicateValue(nums))

nums = [1, 2, 3, 4, 5, 6]
print(firstDuplicateValue(nums))
