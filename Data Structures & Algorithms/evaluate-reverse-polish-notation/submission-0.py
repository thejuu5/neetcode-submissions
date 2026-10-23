class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operator = { '+' : lambda a, b : a + b,
                     '-' : lambda a, b : b - a,
                     '*' : lambda a, b : a * b,
                     '/' : lambda a, b : int(b / a) }
        for s in tokens:
            if s not in operator:
                stack.append(int(s))
            else:
                a = stack.pop()
                b = stack.pop()
                result = operator[s](a,b)
                stack.append(result)
        
        return stack[-1]


        