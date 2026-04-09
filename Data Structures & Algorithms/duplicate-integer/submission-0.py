class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hasAppeared = set()
        for num in nums:
            if num in hasAppeared:
                return True
            else:
                hasAppeared.add(num)
        return False 