from math import sqrt, floor

# 128 ms

# from https://blog.csdn.net/qq_17550379/article/details/80875782
class Solution:

    _dp = [0]
    def numSquares(self, n: int) -> int:
        dp = self._dp

        while len(dp) <= n:
            # -i*i 是为了了得到 i**2, 加负号是直接剪掉了这个值
            dp += list((min(dp[-i*i] for i in range(1, int(len(dp)**0.5+1))) + 1,))
        return dp[n]


if __name__ == "__main__":
    sol = Solution()
    print(sol.numSquares(12))
    