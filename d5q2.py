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
