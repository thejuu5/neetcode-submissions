class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1 
        high = max(piles)
        result = max(piles)
        while low <= high:
            mid = (low + high) // 2
            total_hours = sum((p+mid-1) // mid for p in piles)
            if total_hours > h:
                low = mid + 1
            else:
                result = mid
                high = mid - 1

        return result
        



        