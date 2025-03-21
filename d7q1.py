"""
Valid Triangle Number

Given an integer array nums, return the number of triplets chosen from the array that can make triangles if we take them as side lengths of a triangle.

 

Example 1:

Input: nums = [2,2,3,4]
Output: 3
Explanation: Valid combinations are: 
2,3,4 (using the first 2)
2,3,4 (using the second 2)
2,2,3
Example 2:

Input: nums = [4,2,3,4]
Output: 4
 """



class Solution(object):
    def triangleNumber(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        nums.sort()
        new=[]
        count=0
        n=len(nums)
        for i in range(n):
            for j in range(i+1, n):
                for k in range(j+1,n):
                   
                    if nums[i] + nums[j] > nums[k]:
                        count=count+1
     

        return count
    



l=[2,2,3,4]
print(Solution.triangleNumber(l)) #3
k=[4,2,3,4]
print(Solution.triangleNumber(k)) #4