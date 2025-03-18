# Question 4: Find First and Last Position of Element in Sorted Array.
# Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.
# If target is not found in the array, return [-1, -1].
# Test Cases
# Example 1:
# Input: nums = [5,7,7,8,8,10], target = 8
# Output: [3,4]
# Example 2:
# Input: nums = [5,7,7,8,8,10], target = 6
# Output: [-1,-1]
# Example 3:
# Input: nums = [], target = 0
# Output: [-1,-1]

def position(Ist: list[int], t: int) -> list[int]:
    first, last = -1, -1
    for i in range(len(Ist)):
        if Ist[i] == t:
            if first == -1:  
                first = i
            last = i 

    return [first, last]


print(position([5, 7, 7, 8, 8, 10], 8))  
# Expected Output: [3, 4]

print(position([5, 7, 7, 8, 8, 10], 6))  
# Expected Output: [-1, -1]

print(position([2, 2, 2, 2, 2], 2))  
# Expected Output: [0, 4]


print(position([], 0))  
# Expected Output: [-1, -1]


print(position([4, 4, 5, 6, 7, 4, 4], 4))  
# Expected Output: [0, 6]

