from typing import List


class UnionFind:
    def __init__(self, grid):
        n, m = len(grid), len(grid[0])

        self.count = 0
        self.parent = [-1 for i in range(n*m)]
        self.rank = [0 for i in range(n*m)]
        # self.parent = [-1] * (n*m)
        # self.rank = [0] * (n*m)
        for i in range(n):
            for j in range(m):
                if grid[i][j] == '1':
                    self.parent[i*m+j] = i*m+j
                    self.count += 1

    def find(self, i):
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, x, y):
        rootx = self.find(x)
        rooty = self.find(y)
        if rootx != rooty:
            if self.rank[rootx] > self.rank[rooty]:
                self.parent[rooty] = rootx
            elif self.rank[rootx] < self.rank[rooty]:
                self.parent[rootx] = rooty
            else:
                self.parent[rooty] = rootx
                self.rank[rootx] += 1
            self.count -= 1


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        '''
        20191005
        执行用时 :236 ms, 在所有 Python3 提交中击败了36.28% 的用户
        内存消耗 :16.1 MB, 在所有 Python3 提交中击败了11.82%的用户

        基本是照抄了覃超算法视频里的代码, 算是学习了并查集,
        此处并查集的父节点用了一个一维数组来表示, 有点东西的, 在传入位置的时候麻烦一点, 但是也省去了后面的大量麻烦
        并查集的思路还是相当清晰的, 查看两个节点是否属于同一族, 如果不是则聚合
        '''
        if not grid or not grid[0]:
            return 0

        unionfind = UnionFind(grid)

        vs = [-1, 0, 1, 0]
        hs = [0, -1, 0, 1]
        n, m = len(grid), len(grid[0])

        for i in range(n):
            for j in range(m):
                if grid[i][j] == '0':
                    continue
                for step in range(4):
                    ni, nj = i+vs[step], j+hs[step]
                    if 0<=ni<n and 0<=nj<m and grid[ni][nj] == '1':
                        unionfind.union(m*i+j, m*ni+nj)

        return unionfind.count
        

if __name__ == "__main__":
    sol = Solution()

    ilands = [
        ["1"],
        ["1"],
    ]
    print(sol.numIslands(ilands))

    ilands = [
        ["1"],
        ["1"],
    ]
    print(sol.numIslands(ilands))
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