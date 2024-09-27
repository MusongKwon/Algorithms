# Musong Kwon
# February 25, 2024
# Assignment 2: Find Max Subarray
import math
import random

# max subarray regardless of crossing midpoint
def find_max_subarray(A, low, high):
    if high == low:
        return (low, high, A[low - 1])
    else:
        mid = math.floor((low + high) / 2)
        (left_low, left_high, left_sum) = find_max_subarray(A, low, mid)
        (right_low, right_high, right_sum) = find_max_subarray(A, mid + 1, high)
        (cross_low, cross_high, cross_sum) = find_max_crossing_subarray(A, low, mid, high)
        if left_sum >= right_sum and left_sum >= cross_sum:
            return (left_low, left_high, left_sum)
        elif right_sum >= left_sum and right_sum >= cross_sum:
            return (right_low, right_high, right_sum)
        else: return (cross_low, cross_high, cross_sum)

# max subarray that crosses midpoint
def find_max_crossing_subarray(A, low, mid, high):
    left_sum = float('-inf')
    _sum = 0
    for i in range (mid, low - 1, -1):
        _sum = _sum + A[i - 1]
        if _sum > left_sum:
            left_sum = _sum
            max_left = i
    right_sum = float('-inf')
    _sum = 0
    for j in range (mid + 1, high + 1):
        _sum = _sum + A[j - 1]
        if _sum > right_sum:
            right_sum = _sum
            max_right = j
    return (max_left, max_right, left_sum + right_sum)

# 100 days of randomly generated prices
prices = []
for x in range (0, 100):
    n = random.randint(50, 120)
    prices.append(n)

# changes in prices
changes = [0]*100
for y in range (1, len(prices)):
    changes[y] = prices[y] - prices[y - 1]

# output
print('list of prices: ', prices)
print('list of changes in prices: ', changes)
print('low/high index and largest sum: ', find_max_subarray(changes, 1, len(changes)))