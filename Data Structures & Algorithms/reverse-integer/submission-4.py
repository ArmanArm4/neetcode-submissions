class Solution:
    def reverse(self, x: int) -> int:
        sign = 1
        if x<0:
            sign = -1
            x = -1*x
        if x == 0:
            return 0
        x_length = int(math.log10(x))
        val = 0
        for i in range(x_length,-1,-1):
            k= int(x/(10**i))
            if i== 0:
                k = x
            x -= k*10**i
            val +=k*10**(x_length - i)
        if val >= 2**31 or val < -2**31:
            return 0
        return sign * val