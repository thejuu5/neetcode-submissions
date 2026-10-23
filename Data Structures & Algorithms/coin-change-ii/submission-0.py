class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        memo = {}
        def OPT(i, j):
            if i == 0:
                return 0
            if j == 0:
                return 1
            if (i,j) in memo:
                return memo[(i,j)]
            if coins[i-1] > j:
                result = OPT(i-1,j)
            else:
                result = OPT(i, j - coins[i-1]) + OPT(i-1,j)
            memo[(i,j)] = result
            return result
        return OPT(len(coins), amount)
          

        