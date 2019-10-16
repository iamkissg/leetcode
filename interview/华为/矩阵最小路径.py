from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0
        
        n, m = len(grid), len(grid[0])
        dp = [[0 for _ in range(m)] for _ in range(n)]
        dp[n-1][m-1] = grid[n-1][m-1]
        for i in range(n-2, -1, -1):
            dp[i][m-1] = grid[i][m-1]+dp[i+1][m-1]
        for j in range(m-2, -1, -1):
            dp[n-1][j] = grid[n-1][j]+dp[n-1][j+1]
        
        # for row in dp:
        #     print(row)
        
        for i in range(n-2, -1, -1):
            for j in range(m-2, -1, -1):
                dp[i][j] = grid[i][j] + min(dp[i+1][j], dp[i][j+1])

        # for row in dp:
        #     print(row)

        return dp[0][0]


if __name__ == "__main__":
    sol = Solution()
    print(sol.minPathSum([
        [1,3,1],
        [1,5,1],
        [4,2,1]
    ]))
    print(sol.minPathSum([
        [1,3,],
        [1,5,],
    ]))