"""MAXIMUM GAP
Given an integer array nums, return the maximum difference between two successive elements in its sorted form. If the array contains less than two elements, return 0.

You must write an algorithm that runs in linear time and uses linear extra space.
"""

class Solution(object):
    def maximumGap(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        new=[]
        if len(nums)<2:
            return 0
        
        nums.sort(reverse=True)
        print(nums)
        for i in range(len(nums)-1):
            a=nums[i]-nums[i+1]
            
            new.append(a)
        return max(new)    


a=[3,6,9,1]
print(Solution.maximumGap(a))
