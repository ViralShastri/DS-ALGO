'''
Linear Approch
--------------
Time - O(N) Every Element would Traverse one time two time in worst case
Space - O(1)
'''


def longestPeak(nums):
    maxPeakLength = 0
    for i in range(1, len(nums) - 1):
        if nums[i] > nums[i - 1] and nums[i] > nums[i + 1]:
            currPeakLength = 1
            for j in reversed(range(0, i)):
                if nums[j + 1] <= nums[j]:
                    break
                currPeakLength += 1
            for k in range(i + 1, len(nums)):
                if nums[k] >= nums[k - 1]:
                    break
                currPeakLength += 1
            maxPeakLength = max(currPeakLength, maxPeakLength)
    return maxPeakLength


nums = [1, 2, 3, 3, 4, 0, 10, 6, 5, -1, -3, 2, 3]
print(longestPeak(nums))


nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(longestPeak(nums))

nums = [9, 8, 7, 6, 5, 4, 3, 2, 1]
print(longestPeak(nums))


nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 8]
print(longestPeak(nums))
