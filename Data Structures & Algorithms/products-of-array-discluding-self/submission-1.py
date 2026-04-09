class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        products = []
        loops = 0
        for i in range(len(nums)):
            while loops < len(nums):
                if loops != i:
                    product *= nums[loops]
                loops += 1
            products.append(product)
            product = 1
            loops = 0
        return products
        
                

                
        