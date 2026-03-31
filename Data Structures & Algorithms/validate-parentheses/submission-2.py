class Solution:
    def isValid(self, s: str) -> bool:
        
        map={
            "}":"{",
            "]":"[",
            ")":"("
        }
        stack=[]

        for c in s:
            if c in map:
                if stack and stack.pop()==map[c]:
                    continue
                else:
                    return False
            else:
                stack.append(c)
        return True if not stack else False