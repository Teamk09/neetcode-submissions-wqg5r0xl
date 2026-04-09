class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(t) != len(s):
            return False
        
        letCountT = {}
        letCountS = {}
        for let in t:
            letCountT[let] = letCountT.get(let, 0) + 1

        for let in s:
            letCountS[let] = letCountS.get(let, 0) + 1
        
        return letCountT == letCountS
            