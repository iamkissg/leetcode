from typing import List


class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        '''
        20191002
        44 ms	13.9 MB	Python3

        沿用了石子游戏的代码, 完全不用改
        '''
        n = len(nums)

        dp = [[[0, 0] for _ in range(n)] for _ in range(n)]

        # base case
        for i in range(n):
            dp[i][i][0] = nums[i]
            dp[i][i][1] = 0

        # l 是石头堆的个数, base case 已经覆盖了一堆石头的情况, 因此从两堆开始到 n 堆
        # i 是石头的堆的左边索引, j 是右边索引
        for l in range(2, n+1):
            for i in range(n-l+1):
                j = l+i-1

                # 先手取左边或取右边, 然后转为后手取
                left = nums[i] + dp[i+1][j][1]
                right = nums[j] + dp[i][j-1][1]
                
                # 先手取左边的值更大, 此时对手后手取, 相当于他先手从剩下堆中取
                if left > right:
                    dp[i][j][0] = left
                    dp[i][j][1] = dp[i+1][j][0]
                # 先手取右边的值更大
                else:
                    dp[i][j][0] = right
                    dp[i][j][1] = dp[i][j-1][0]
        
        res = dp[0][n-1]
        return (res[0] - res[1]) >= 0


if __name__ == "__main__":
    sol = Solution()
    print(sol.PredictTheWinner([5,3,4,5]))
    print(sol.PredictTheWinner([1, 5, 2]))
    print(sol.PredictTheWinner([1, 5, 233, 7]))