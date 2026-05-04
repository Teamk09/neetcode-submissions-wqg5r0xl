class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) == 1:
            return True
        
        l, r = 0, len(s)-1

        sLower = s.lower()

        while l<r:
            while not sLower[l].isalnum() and l<r:
                l += 1
            while not sLower[r].isalnum() and l<r:
                r -= 1
        
            print(sLower[l])
            print(sLower[r])
            if sLower[l] != sLower[r]:
                return False
            l += 1
            r -= 1
        return True
