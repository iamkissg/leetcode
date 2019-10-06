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
        
        M = 1
        max_val = self.help(piles, M)

    def help(self, piles: List[int], M):
        if not piles:
            return 0
        elif len(piles) == 1:
            return piles[0]

        ans = piles[:M]
        MAX_X = 2 * M
        for i in range(1, MAX_X):
            rest = sum(piles[M:]) - self.helper(piles[M:], i)
            ans

if __name__ == "__main__":
    sol = Solution()
    print(sol.stoneGame([5,3,4,5]))
    print(sol.stoneGame([2,7,9,4,4]))