class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        sorted_list = sorted(zip(position,speed),reverse = True)
        for pos, spd in sorted_list:
            time = (target - pos) / spd
            if not stack:
                stack.append(time)
            elif time > stack[-1]:
                stack.append(time)
            else:
                continue
        return len(stack)

           


        