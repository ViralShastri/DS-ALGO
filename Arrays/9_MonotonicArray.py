'''
Linear Approch
--------------
Time - O(n)
Space - O(1)
'''


def monotonicArray(nums):
    isNonIncreasing = True
    isNonDecreasing = True

    for i in range(len(nums) - 1):
        if nums[i] < nums[i + 1]:
            isNonIncreasing = False

        if nums[i] > nums[i + 1]:
            isNonDecreasing = False

    return isNonIncreasing or isNonDecreasing


nums = [1, 2, 2, 3]
print(monotonicArray(nums))

nums = [6, 5, 4, 4]
print(monotonicArray(nums))

nums = [1, 3, 2]
print(monotonicArray(nums))

nums = [1, 2, 4, 5]
print(monotonicArray(nums))

nums = [1, 1, 1]
print(monotonicArray(nums))
