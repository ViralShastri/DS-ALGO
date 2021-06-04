'''
Optimal Approch
--------------
Time - O(NlogN) // Sorting Array
Space - O(1) 
'''


def nonConstructibleChange(coins):
    coins.sort()
    change = 0
    for coin in coins:
        if coin > change + 1:
            return change + 1
        change = change + coin
    return change + 1


coins = [5, 7, 1, 1, 2, 3, 22]
print(nonConstructibleChange(coins))

coins = [1, 2, 3, 4, 5]
print(nonConstructibleChange(coins))
