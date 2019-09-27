from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices or len(prices) == 1:
            return 0
        # 股票价格一直在降的情况
        elif sorted(prices, reverse=True) == prices:
            return 0

        max_profit = 0
        acculated_profit = 0
        low = prices[0]
        for p in prices[:-1]:
            if p < low:
                low = p  # buy
                if max_profit > 0:
                    acculated_profit += max_profit
                    max_profit = 0
            if p - low > max_profit:
                max_profit = p - low
                continue
            if max_profit > 0:
                low = p
                acculated_profit += max_profit
                max_profit = 0
        acculated_profit += prices[-1] - low if prices[-1] - low > max_profit else max_profit
        return acculated_profit

    def maxProfit_greedy(self, prices: List[int]) -> int:
        '''
        20190924
        '''
        profit = 0
        for i, p in enumerate(prices[:-1]):
            if p < prices[i+1]:
                profit += prices[i+1] - p
        return profit


if __name__ == "__main__":
    sol = Solution()
    print(sol.maxProfit([0]))
    print(sol.maxProfit_greedy([0]))
    print(sol.maxProfit([1]))
    print(sol.maxProfit_greedy([1]))
    print(sol.maxProfit([]))
    print(sol.maxProfit_greedy([]))
    print(sol.maxProfit([7,6,4,3,1]))
    print(sol.maxProfit_greedy([7,6,4,3,1]))
    print(sol.maxProfit([1,2,3,4,5]))
    print(sol.maxProfit_greedy([1,2,3,4,5]))
    print(sol.maxProfit([7,1,5,3,6,4]))
    print(sol.maxProfit_greedy([7,1,5,3,6,4]))
    print(sol.maxProfit([1,2,4,2,5,7,2,4,9,0]))
    print(sol.maxProfit_greedy([1,2,4,2,5,7,2,4,9,0]))
    print(sol.maxProfit([2,1,2,0,1]))
    print(sol.maxProfit_greedy([2,1,2,0,1]))
            
