class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            x = 1 / x
            n = 0 - n
        num = 1
        while n > 0:
            num *= x
            n -= 1

        return num
