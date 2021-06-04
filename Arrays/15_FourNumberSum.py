'''
Quadratic Approch
--------------
Time - O(N^2) Worst - O(N^3)
Space - O(N^2)
'''


def fourNumberSum(nums, target):
    hashTable = {}
    result = []

    for i in range(1, len(nums) - 1):
        for j in range(i+1, len(nums)):
            currentSum = nums[i] + nums[j]
            difference = target - currentSum

            if difference in hashTable:
                for pair in hashTable[difference]:
                    result.append(pair + [nums[i], nums[j]])

        for k in range(i):
            currentSum = nums[k] + nums[i]
            if currentSum not in hashTable:
                hashTable[currentSum] = []
            hashTable[currentSum].append([nums[k], nums[i]])

    return result


nums = [7, 6, 4, -1, 1, 2]
target = 16
print(fourNumberSum(nums, target))
