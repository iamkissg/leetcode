from typing import List


class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        '''
        20191002
        720 ms	39.4 MB	Python3

        直接学得 labuladong 的算法, 用动态规划的方法来解决博弈问题
        用一个二维的 dp table, 表示从 i-j (包括j)的数中取值, 而 dp[i][j] 又是一个二元组, 分别表示先后手能取得的累计最高值
        base case 比较好理解, 只有一个可选数的时候, 先手拿到, 后手没有
        然后在多一堆的情况下, 缓缓地递推, 直到囊括整个数组
        '''
        n = len(piles)

        dp = [[[0, 0] for _ in range(n)] for _ in range(n)]

        # base case
        for i in range(n):
            dp[i][i][0] = piles[i]
            dp[i][i][1] = 0

        # l 是石头堆的个数, base case 已经覆盖了一堆石头的情况, 因此从两堆开始到 n 堆
        # i 是石头的堆的左边索引, j 是右边索引
        for l in range(2, n+1):
            for i in range(n-l+1):
                j = l+i-1

                # 先手取左边或取右边, 然后转为后手取
                left = piles[i] + dp[i+1][j][1]
                right = piles[j] + dp[i][j-1][1]
                
                # 先手取左边的值更大, 此时对手后手取, 相当于他先手从剩下堆中取
                if left > right:
                    dp[i][j][0] = left
                    dp[i][j][1] = dp[i+1][j][0]
                # 先手取右边的值更大
                else:
                    dp[i][j][0] = right
                    dp[i][j][1] = dp[i][j-1][0]
        
        res = dp[0][n-1]
        return (res[0] - res[1]) > 0


if __name__ == "__main__":
    sol = Solution()
    print(sol.stoneGame([5,3,4,5]))