class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        for num in nums:
            counts[num] = counts.get(num, 0) + 1
        
        bucket = [[] for i in range(len(nums) + 1)]

        for num, c in counts.items():
            bucket[c].append(num)
        
        final = []
        for i in range(len(bucket) - 1, 0, -1):
            if bucket[i]:
                for val in bucket[i]:
                    final.append(val)
        return final[:k]
