class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        sDict = {}
        tDict = {}
        for i, let in enumerate(s):
            if let in sDict:
                sDict[let] += 1
            else:
                sDict[let] = 1
        
        for i, let in enumerate(t):
            if let in tDict:
                tDict[let] += 1
            else:
                tDict[let] = 1
        
        if sDict == tDict:
            return True
        else:
            return False 