'''
Quadratic Approch
--------------
Time - O(N^2)
Space - O(N)
'''


def threeNumberSum(nums, target):
    nums.sort()
    result = []
    for i in range(len(nums) - 2):
        left = i + 1
        right = len(nums) - 1

        while left < right:
            if nums[i] + nums[left] + nums[right] == target:
                result.append([nums[i], nums[left], nums[right]])
                left += 1
                right -= 1
                continue

            elif nums[i] + nums[left] + nums[right] < target:
                left += 1

            elif nums[i] + nums[left] + nums[right] > target:
                right -= 1

    return result


nums = [12, 3, 1, 2, -6, 5, -8, 6]
target = 0
print(threeNumberSum(nums, target))

nums = [12, 3, 1, 2, -6, 5, -8, 6]
target = 6
print(threeNumberSum(nums, target))
