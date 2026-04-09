class Solution:

    def encode(self, strs: List[str]) -> str:
        message = ""
        for s in strs:
            message += str(len(s)) + "$" + s
        return message


    def decode(self, s: str) -> List[str]:
        l, r = 0, 0
        words = []
        while r < len(s):
            while s[r] != "$":
                r += 1
            wordLen = int(s[l:r])

            start = r + 1
            end = r + 1 + wordLen
            words.append(s[start:end])
            
            l = end
            r = end
            
        return words

