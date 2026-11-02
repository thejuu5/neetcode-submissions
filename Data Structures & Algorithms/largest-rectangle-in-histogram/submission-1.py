class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0
        for i in range(len(heights)):
            while stack and heights[i] < heights[stack[-1]]:
                element = stack.pop()
                if not stack:
                    width = i
                    area = heights[element] * width
                else:
                    width = i - stack[-1] - 1
                    area = heights[element] * width
                if area > max_area:
                    max_area = area
          
            stack.append(i)
        
        while stack:
            num = stack.pop()
            if not stack:
                width = len(heights)
                area = heights[num] * width
            else:
                width = len(heights) - stack[-1] - 1
                area = heights[num] * width
            if area > max_area:
                max_area = area

        return max_area

                


            
        