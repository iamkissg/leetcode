from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices or len(prices) == 1:
            return 0

        # 股票价格一直在降的情况
        if sorted(prices, reverse=True) == prices:
            return 0

        for 



if __name__ == "__main__":
    sol = Solution()
    print(sol.maxProfit([0]))
    print(sol.maxProfit([1]))
    print(sol.maxProfit([]))
    print(sol.maxProfit([7,6,4,3,1]))
    print(sol.maxProfit([1,2,3,4,5]))
    print(sol.maxProfit([7,1,5,3,6,4]))
    print(sol.maxProfit([1,2,4,2,5,7,2,4,9,0]))
    print(sol.maxProfit([2,1,2,0,1]))
            
