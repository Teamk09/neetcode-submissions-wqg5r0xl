class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        sDict = {}
        tDict = {}
        for let in s:
            if let in sDict:
                sDict[let] += 1
            else:
                sDict[let] = 1
        
        for let in t:
            if let in tDict:
                tDict[let] += 1
            else:
                tDict[let] = 1
        
        return sDict == tDict