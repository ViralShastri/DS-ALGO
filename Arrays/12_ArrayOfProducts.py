'''
Linear Approch
--------------
Time - O(N)
Space - O(N)
'''


def arrayOfProducts(nums):
    result = [1] * len(nums)

    currLeftProudct = 1
    for i in range(len(nums)):
        result[i] = currLeftProudct
        currLeftProudct *= nums[i]

    currRightProudct = 1
    for j in reversed(range(len(nums))):
        result[j] *= currRightProudct
        currRightProudct *= nums[j]

    return result


nums = [1, 2, 3, 4]
print(arrayOfProducts(nums))

nums = [-1, 1, 0, -3, 3]
print(arrayOfProducts(nums))
