from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices or len(prices) == 1:
            return 0
        elif sorted(prices, reverse=True) == prices:
            return 0

        low = prices[0]
        max_profit = 0
        for p in prices:
            if p < low:
                low = p
                continue
            max_profit = max(p - low, max_profit)
        return max_profit



if __name__ == "__main__":
    sol = Solution()
    print(sol.maxProfit([0]))
    print(sol.maxProfit([1]))
    print(sol.maxProfit([]))
    print(sol.maxProfit([7,6,4,3,1]))
    print(sol.maxProfit([7,1,5,3,6,4]))