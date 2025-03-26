"""
Given a binary array nums, return the maximum number of consecutive 1's in the array if you can flip at most one 0.

Test Cases
Example 1:
Input: nums = [1, 0, 1, 1, 0]

Output: 4

Explanation:

Flip the first 0 → [1, 1, 1, 1, 0] → 4 consecutive 1s

Flip the second 0 → [1, 0, 1, 1, 1] → 3 consecutive 1s

Max = 4

Example 2:
Input: nums = [1, 0, 1, 1, 0, 1]

Output: 4

Explanation:

Flip either 0 → max streak becomes 4
"""



from typing import List

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        left = 0
        zero_count = 0
        max_length = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                zero_count += 1

            while zero_count > 1:
                if nums[left] == 0:
                    zero_count -= 1
                left += 1

            max_length = max(max_length, right - left + 1)

        return max_length


#Usage Example:
sol = Solution()

input1 = [1, 0, 1, 1, 0]
input2 = [1, 1, 0, 1]
input3 = [0, 1, 0, 1, 0, 1, 0]
input4 = [1, 1, 1, 0, 1, 1, 1]

print(sol.findMaxConsecutiveOnes(input1))  # Output: 4
print(sol.findMaxConsecutiveOnes(input2))  # Output: 4
print(sol.findMaxConsecutiveOnes(input3))  # Output: 3
print(sol.findMaxConsecutiveOnes(input4))  # Output: 7