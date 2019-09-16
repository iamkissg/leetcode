from math import sqrt, floor


'''Lagrange 四平方定理： 任何一个正整数都可以表示成不超过四个整数的平方之和。'''

# from https://blog.csdn.net/qq_17550379/article/details/80875782
class Solution:

    _dp = [0]
    def numSquares(self, n: int) -> int:
        dp = self._dp

        while len(dp) <= n:
            for i in range(1, int(len(dp)**0.5+1)):
                # dp[-i*i] ???
                dp += list((min(dp[-i*i] for i in range(1, int(len(dp)**0.5+1))) + 1,))
        return dp[n]


if __name__ == "__main__":
    sol = Solution()
    print(sol.numSquares(12))
    