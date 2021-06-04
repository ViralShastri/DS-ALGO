'''
Linear Approch
--------------
Time - O(NlogN) - Sorting Intervals
Space - O(N)
'''


def mergeOverlappingIntervals(intervals):
    intervals = sorted(intervals, key=lambda x: x[0])

    result = []

    result.append(intervals[0])
    poniter = 0
    for i in range(1, len(intervals)):
        if result[poniter][1] >= intervals[i][0]:
            if result[poniter][1] < intervals[i][1]:
                result[poniter][1] = intervals[i][1]
        else:
            result.append(intervals[i])
            poniter += 1
    return result


intervals = [[1, 2], [3, 5], [4, 7], [6, 8], [9, 10]]
print(mergeOverlappingIntervals(intervals))

intervals = [[1, 2], [4, 7], [9, 10], [6, 8], [3, 5]]
print(mergeOverlappingIntervals(intervals))

intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
print(mergeOverlappingIntervals(intervals))

intervals = [[1, 4], [4, 5]]
print(mergeOverlappingIntervals(intervals))

intervals = [[1, 4], [2, 3]]
print(mergeOverlappingIntervals(intervals))
