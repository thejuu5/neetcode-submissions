class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        sorted_list = sorted(zip(position,speed),reverse = True)
        for pos, spd in sorted_list:
            distance = (target - pos) / spd
            if not stack:
                stack.append(distance)
            elif distance > stack[-1]:
                stack.append(distance)
            else:
                continue
        return len(stack)

           


        