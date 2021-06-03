'''
Quadratic Approch
--------------
Time - O(N^2)
Space - O(1)
'''

#     def twoNumberSum(self, nums: List[int], target: int) -> List[int]:
#       for i in range(len(nums)):
#           for j in range(i + 1, len(nums)):
#               if nums[i] + nums[j] == target:
#                   return [i, j]
#       return []


'''
Linear Approch
--------------
Time - O(n)
Space - O(n)
'''


def twoNumberSum(nums, target):
    hashTable = dict()
    for i in range(len(nums)):
        secNum = target - nums[i]
        if secNum in hashTable:
            return [hashTable[secNum], i]
        hashTable[nums[i]] = i
    return []


'''
Linear Approch
--------------
Time - O(NlogN)
Space - O(1)
'''

# Not Working when returning Index

#     def twoNumberSum(self, nums: List[int], target: int) -> List[int]:
#         nums.sort()
#         left = 0
#         right = len(nums) - 1

#         while left < right:
#             if nums[left] + nums[right] == target:
#                 return [left, right]

#             elif nums[left] + nums[right] < target:
#                 left += 1

#             elif nums[left] + nums[right] > target:
#                 right -= 1

#         return []


nums = [2, 7, 11, 15]
target = 9
print(twoNumberSum(nums, target))

nums = [3, 2, 4]
target = 6
print(twoNumberSum(nums, target))

nums = [3, 3]
target = 6
print(twoNumberSum(nums, target))

nums = [3]
target = 6
print(twoNumberSum(nums, target))

nums = [6]
target = 6
print(twoNumberSum(nums, target))

nums = [3, 4]
target = 6
print(twoNumberSum(nums, target))
