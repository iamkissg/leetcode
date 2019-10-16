from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices or len(prices) < 2:
            return 0

        n = len(prices)
        dp = [0 for i in range(n)]
        min_pre = prices[0]
        for i, p in enumerate(prices[1:], start=1):
            if p-min_pre > dp[i-1]:
                dp[i] = p-min_pre
            else:
                dp[i] = dp[i-1]
            min_pre = min(p, min_pre)
        return dp[-1]


if __name__ == "__main__":
    sol = Solution()
    print(sol.maxProfit([7,1,5,3,6,4]))
    print(sol.maxProfit([7,6,4,3,1]))