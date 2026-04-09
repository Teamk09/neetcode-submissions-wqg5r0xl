class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        letDict = {}
        for i in range(len(s)):
            letDict[s[i]] = letDict.get(s[i], 0) + 1
            letDict[t[i]] = letDict.get(t[i], 0) - 1
        
        for val in letDict.values():
            if val != 0:
                return False
        return True