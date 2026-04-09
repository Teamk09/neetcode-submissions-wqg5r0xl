class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groupDict = {}
        for word in strs:
            count = [0] * 26

            for let in word:
                count[ord(let) - ord("a")] += 1
            
            key = tuple(count)
            if key not in groupDict:
                groupDict[key] = []
            groupDict[key].append(word)

        return list(groupDict.values())