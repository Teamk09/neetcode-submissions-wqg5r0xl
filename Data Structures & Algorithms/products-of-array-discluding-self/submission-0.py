class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        products = []
        loops = 0
        seeker = 0
        for i in range(len(nums)):
            while loops < len(nums):
                if seeker != i:
                    product *= nums[seeker]
                loops += 1
                seeker += 1
            products.append(product)
            product = 1
            seeker = 0
            loops = 0
        return products
        
                

                
        