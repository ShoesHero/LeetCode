class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2

        x = 1
        y = 2
        z = 0
        for i in range(3, n+1):
            z = x + y
            x = y
            y = z
        return z