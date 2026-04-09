class Solution:

    def encode(self, strs: List[str]) -> str:
        message = ""
        code = "&$#@"
        for s in strs:
            message += s + code
        return message


    def decode(self, s: str) -> List[str]:
        words = s.split("&$#@")
        return words[:-1]
