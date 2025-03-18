class Solution(object):
    def minSubArrayLen(target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        left = 0
        min_length = float('inf')
        current_sum = 0
        
        for right in range(n):
            current_sum += nums[right]
            
            while current_sum >= target:
                min_length = min(min_length, right - left + 1)
                current_sum -= nums[left]
                left += 1
        return min_length if min_length != float('inf') else 0
    

# Test Case 1: target = 7, nums = [2, 3, 1, 2, 4, 3]
print(Solution.minSubArrayLen(7, [2, 3, 1, 2, 4, 3]))  # Output: 2

# Test Case 2: target = 4, nums = [1, 4, 4]
print(Solution.minSubArrayLen(4, [1, 4, 4]))  # Output: 1

# Test Case 3: target = 11, nums = [1, 1, 1, 1, 1, 1, 1, 1]
print(Solution.minSubArrayLen(11, [1, 1, 1, 1, 1, 1, 1, 1]))  # Output: 0
