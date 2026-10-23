class Solution:
    def getSum(self, a: int, b: int) -> int:
        carry = 1
        while(carry != 0):
            total = a ^ b
            carry = (a & b) << 1
            total = total & 0xFFFFFFFF
            carry = carry & 0xFFFFFFFF
            a = total
            b = carry
        
        if total >= 0x80000000:
            return total - 0x100000000
        else: 
            return total