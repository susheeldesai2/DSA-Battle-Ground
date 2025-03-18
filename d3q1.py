class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        length = len(nums)
        products = [1] * length
        for i in range(1, length):
            products[i] = products[i-1] * nums[i-1]

        right = nums[-1]
        for i in range(length-2, -1, -1):
            products[i] *= right
            right *= nums[i]
        
        return products


    #     def product_array_except_self(nums):
    # n = len(nums)
    # result = []
    
    # for i in range(n):
    #     product = 1  # Initialize the product 
        
    #     for j in range(n):
    #         if i != j:
    #             product *= nums[j]
        
    #     # Append product to result
    #     result.append(product)
    
    # return result