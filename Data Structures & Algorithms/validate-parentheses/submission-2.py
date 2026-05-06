from collections import deque
class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 1:
            return False
        stack = deque()
        pairs = { ")" : "(", "]" : "[", "}" : "{" }
        for let in s:
            print(let)
            if let in pairs:
                print("inside")
                if stack and stack[-1] == pairs[let]:
                    print("why not here")
                    stack.pop()
                else:
                    return False
            else:
                stack.append(let)   
        if not stack:
            return True
        else:
            return False