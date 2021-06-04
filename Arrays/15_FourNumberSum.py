'''
Linear Approch
--------------
Time - O(N) - Big N - Traversal of each Ele in Matrix
Space - O(N)
'''


def SpiralTraverse(matrix):
    sRow = 0
    sCol = 0
    eRow = len(matrix) - 1
    eCol = len(matrix[0]) - 1
    result = []

    while sRow <= eRow and sCol <= eCol:
        for c in range(sCol, eCol + 1):
            result.append(matrix[sRow][c])

        for r in range(sRow + 1, eRow + 1):
            result.append(matrix[r][eCol])

        for c in reversed(range(sCol, eCol)):
            if sRow == eRow:
                break
            result.append(matrix[eRow][c])

        for r in reversed(range(sRow + 1, eRow)):
            if sCol == eCol:
                break
            result.append(matrix[r][sCol])

        sRow += 1
        sCol += 1
        eRow -= 1
        eCol -= 1

    return result


matrix = [[1, 2, 3, 4], [12, 13, 14, 5], [11, 16, 15, 6], [10, 9, 8, 7]]
print(SpiralTraverse(matrix))

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(SpiralTraverse(matrix))

matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
print(SpiralTraverse(matrix))
