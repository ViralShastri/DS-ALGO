'''
Naive Approch
--------------
Time - O(NlogN)
Space - O(1)
'''

# def sortedSquares(nums):
#     for i in range(len(nums)):
#         nums[i] = nums[i] ** 2
#     nums.sort()
#     return nums


'''
Linear Approch
--------------
Time - O(n)
Space - O(n)
'''


def sortedSquares(nums):
    sortedSquaresArray = [0] * len(nums)
    small = 0
    large = len(nums) - 1

    for i in reversed(range(len(nums))):
        if abs(nums[small]) > abs(nums[large]):
            sortedSquaresArray[i] = nums[small] ** 2
            small += 1
        else:
            sortedSquaresArray[i] = nums[large] ** 2
            large -= 1

    return sortedSquaresArray


nums = [-4, -1, 0, 3, 10]
print(sortedSquares(nums))

nums = [-7, -3, 2, 3, 11]
print(sortedSquares(nums))

nums = [-5, -3, -2, -1]
print(sortedSquares(nums))
