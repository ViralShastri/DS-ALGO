'''
Optimal Approch
--------------
Time - O(NlogN)
Space - O(1)
'''


def smallestDifference(nums1, nums2):
    nums1.sort()
    nums2.sort()

    left = 0
    right = 0
    minDiff = float("inf")
    minDiffPair = []

    while left < len(nums1) and right < len(nums2):
        diff = abs(nums1[left] - nums2[right])

        if diff < minDiff:
            minDiff = diff
            minDiffPair = [nums1[left], nums2[right]]

        if nums1[left] < nums2[right]:
            left += 1
        elif nums1[left] > nums2[right]:
            right += 1
        else:
            return [nums1[left], nums2[right]]

    return minDiffPair


nums1 = [1, 5, 10, 20, 28, 3]
nums2 = [26, 134, 135, 15, 17]
print(smallestDifference(nums1, nums2))

nums1 = [1, 2, 3, 4, 5, 6]
nums2 = [10]
print(smallestDifference(nums1, nums2))
