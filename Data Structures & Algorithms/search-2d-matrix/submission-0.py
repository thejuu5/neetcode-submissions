class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        low = 0
        m = len(matrix)
        n = len(matrix[0])
        high = m * n - 1
        while low <= high:
            mid = (low + high) // 2
            row = mid // n 
            col = mid % n
            value = matrix[row][col]
            if target == value:
                return True
            elif target > value:
                low = mid + 1
            else:
                high = mid - 1
        

        return False