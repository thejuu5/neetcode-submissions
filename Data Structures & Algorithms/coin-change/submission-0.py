class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
        def OPT(i,j):
            if i == 0:
                return float('inf')
            if j == 0:
                return 0
            if (i,j) in memo:
                return memo[(i,j)]
            if coins[i-1] > j:
                result = OPT(i-1,j)
            else:
                result = min(1 + OPT(i, j - coins[i-1]), OPT(i-1, j))
            memo[(i,j)] = result
            return result
        answer =  OPT(len(coins),amount)
        if answer == float('inf'):
            return -1
        else:
            return answer
    
        
        