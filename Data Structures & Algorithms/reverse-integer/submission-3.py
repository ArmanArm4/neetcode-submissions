class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x < 0 else 1
        x = abs(x)
        val = 0
        while x:
            val = val * 10 + x % 10
            x //= 10
        val *= sign
        if val < -2**31 or val > 2**31 - 1:
            return 0
        return val