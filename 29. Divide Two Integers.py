class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == -2147483648 and divisor == -1:
            return 2147483647
        ans=dividend//divisor
        if ans==0:
            return 0
        if dividend%divisor==0:
            return ans
        if ans>0:
            return math.floor(ans)
        return ans+1
