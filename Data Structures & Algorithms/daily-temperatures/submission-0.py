class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []
        for t in range(len(temperatures)):
            if stack:
                while stack and temperatures[t] > temperatures[stack[-1]]:
                    stack_top = stack[-1]
                    if temperatures[t] > temperatures[stack_top]:
                        result[stack_top]+= t - stack_top
                        stack.pop()
                else:
                    stack.append(t)
            else:
                stack.append(t)

        return result
    

        
        