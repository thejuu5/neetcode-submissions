class Solution:
    def getSum(self, a: int, b: int) -> int:
        carry = 1
        while(carry != 0):
            total = a ^ b
            carry = (a & b) << 1
            total = total & (2**32 - 1)
            carry = carry & (2**32 - 1)
            a = total
            b = carry
        
        if total >= 2**31:
            return total - 2**32
        else: 
            return total