from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        '''
        124 ms	15.2 MB	Python3
        '''
        if not grid or not grid[0]:
            return 0

        n, m = len(grid), len(grid[0])
        if n == 1:
            return sum(g for g in grid[0])
        if m == 1:
            return sum(g[0] for g in grid)

        dp = [[0 for j in range(m)] for i in range(n)]

        # 填好右下角以及底边右边的各格子
        dp[n-1][m-1] = grid[n-1][m-1]
        for i in range(n-2, -1, -1):
            dp[i][m-1] = grid[i][m-1] + dp[i+1][m-1]
        for j in range(m-2, -1, -1):
            dp[n-1][j] = grid[n-1][j] + dp[n-1][j+1]
        
        for i in range(n-2, -1, -1):
            for j in range(m-2, -1, -1):
                dp[i][j] = grid[i][j] + min(dp[i+1][j], dp[i][j+1])

        return dp[0][0]

if __name__ == "__main__":
    sol = Solution()
    print(sol.minPathSum([
  [1,3,1],
  [1,5,1],
  [4,2,1]
]))
    print(sol.minPathSum([
[9,1,4,8]
]))