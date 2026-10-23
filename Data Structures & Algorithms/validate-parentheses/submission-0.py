class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closedParanthesisMap = { ')' : '(' , '}' : '{' , ']' : '['}
        for c in s:
            if c in closedParanthesisMap:
                if stack and stack[-1] == closedParanthesisMap[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        
        if stack:
            return False
        else:
            return True
                

        