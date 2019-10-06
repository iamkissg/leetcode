from typing import List

vs = [-1, 0, 1, 0]
hs = [0, -1, 0, 1]

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0

        count = 0
        n, m = len(grid), len(grid[0])
        for i in range(n):
            for j in range(m):
                if grid[i][j] == '0':
                    continue
                count += 1
                self.destroy(grid, i, j, n, m)
        return count

    def destroy(self, grid, i, j, n, m):
        grid[i][j] = '0'

        for step in range(4):
            if 0<=i+vs[step]<n and 0<=j+hs[step]<m and grid[i+vs[step]][j+hs[step]]=='1':
                self.destroy(grid, i+vs[step], j+hs[step], n, m)
        

if __name__ == "__main__":
    sol = Solution()
    ilands = [
        ["1","1","1","1","0"],
        ["1","1","0","1","0"],
        ["1","1","0","0","0"],
        ["0","0","0","0","0"]
    ]
    print(sol.numIslands(ilands))

    ilands = [
        ["1","1","0","0","0"],
        ["1","1","0","0","0"],
        ["0","0","1","0","0"],
        ["0","0","0","1","1"]
    ]
    print(sol.numIslands(ilands))