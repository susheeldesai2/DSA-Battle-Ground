"""Given a list of non-negative integers nums, arrange them such that they form the largest number and return it.

Since the result may be very large, so you need to return a string instead of an integer.

 

Example 1:

Input: nums = [10,2]
Output: "210"
Example 2:

Input: nums = [3,30,34,5,9]
Output: "9534330""""



from itertools import permutations

def largestNumber_bruteforce(nums):
    # Convert all numbers to strings
    nums = list(map(str, nums))

    # Generate all possible permutations
    all_permutations=permutations(nums)
    permuted_numbers = [''.join(p) for p in all_permutations]
    #return permuted_numbers
    # Convert to integers and find the maximum
    max_number = max(permuted_numbers, key=int)
    
    return max_number

# Example cases
print(largestNumber_bruteforce([10, 2]))        # Expected Output: "210"
print(largestNumber_bruteforce([3, 30, 34, 5, 9]))  # Expected Output: "9534330"
print(largestNumber_bruteforce([0, 0]))         # Expected Output: "0"
