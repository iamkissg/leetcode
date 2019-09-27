from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        '''
        20190925
        为数不多的, 不用费脑子就找出状态定义和状态转移方程的简单题, 有一点成就感呢
        执行用时 :128 ms, 在所有 Python3 提交中击败了19.41% 的用户
        内存消耗 :13.9 MB, 在所有 Python3 提交中击败了5.26%的用户
        '''

        dp = [0, cost[0]]
        for i, c in enumerate(cost[1:], start=2):
            dp.append(min(dp[i-1], dp[i-2]) + c)
        return min(dp[-1], dp[-2])

if __name__ == "__main__":
    sol = Solution()
    print(sol.minCostClimbingStairs([10, 15, 20]))
    print(sol.minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]))