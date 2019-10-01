from typing import List

class Solution:

    def coinChange(self, coins: List[int], amount: int) -> int:
        '''
        20190930
        执行用时 :1744 ms, 在所有 Python3 提交中击败了71.45% 的用户
        内存消耗 :14 MB, 在所有 Python3 提交中击败了7.80%的用户

        这个题目, 看题解看了一个下午+晚上, 看成傻逼了, 就纳闷 cpp 的代码里, dp[i] 的默认值是哪里来的, 苦思不得
        然后才在 Python 的题解里看到了将数组默认初始化为 amount+1 的做法 (一个小技巧, 可能失效, 那就换其他值),
        如此还能方便处理兑换不了零钱的情况.
        '''
        if not coins:
            return -1
        if not amount:
            return 0

        dp = [amount+1 for _ in range(amount+1)]
        dp[0] = 0
        for i in range(1, amount+1):
            for coin in coins:
                if i - coin >= 0:
                    dp[i] = min(dp[i-coin]+1, dp[i])

        return -1 if dp[amount] == amount+1 else dp[amount]


if __name__ == "__main__":
    sol = Solution()
    print(sol.coinChange([1,2,5], 10))
    print(sol.coinChange([1,2,5], 11))
    print(sol.coinChange([2], 3))