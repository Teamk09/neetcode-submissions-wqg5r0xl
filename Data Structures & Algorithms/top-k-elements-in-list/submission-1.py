class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        for num in nums:
            counts[num] = counts.get(num, 0) + 1
        
        buckets = [[] for i in range(len(nums) + 1)]
        
        for num, c in counts.items():
            buckets[c].append(num)

        final = []
        for i in range(len(nums), 0, -1):
            for num in buckets[i]:
                final.append(num)
        
        return final[:k]

            
            

