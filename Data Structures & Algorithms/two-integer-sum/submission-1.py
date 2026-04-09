class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pastNums = {}
        for i, num in enumerate(nums): 
            diff = target - num

            if diff in pastNums:
                return [pastNums[diff], i]
            else:
                pastNums[num] = i
            
        