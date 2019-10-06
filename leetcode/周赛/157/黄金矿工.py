from typing import List


class Solution:
    step_x = [-1, 1, 0, 0]
    step_y = [0, 0, -1, 1]

    def getMaximumGold(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])

        max_gold = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] != 0:
                    gold = self.mine(grid[:], n, m, i, j, {(i, j)})
                    if gold > max_gold:
                        max_gold = gold
        return max_gold

    def mine(self, grid: List[List[int]], n:int, m: int, i: int, j: int, visited) -> int:

        cur= grid[i][j]
        steps = [0]
        for step in range(4):
            ni, nj = i+self.step_x[step], j+self.step_y[step]
            if (ni, nj) in visited: continue
            if 0<=ni<n and 0<=nj<m and grid[ni][nj] > 0:
                # 我有点想差了, 走过的路不能在走了, 仅此而已, 不能把反方向的矿给堵上了, 因为后面顺着路线可以还是可以挖到的
                steps.append(self.mine(grid[:], n, m, ni, nj, visited|{(ni, nj)}))
        return cur + max(steps)
            

if __name__ == "__main__":
    sol = Solution()
    print(sol.getMaximumGold(grid = [[0,6,0],[5,8,7],[0,9,0]]))
    print(sol.getMaximumGold(grid = [[1,0,7],[2,0,6],[3,4,5],[0,3,0],[9,0,20]]))
    # 491
    print(sol.getMaximumGold([
        [0,12,18,0,10,2,28,28],
        [6,21,38,35,36,3,22,28],
        [34,4,33,0,14,0,29,13],
        [25,28,7,0,10,0,31,0]]))
    print(sum([sum([0,12,18,0,10,2,28,28]), sum([6,21,38,35,36,3,22,28]), sum([34,4,33,0,14,0,29,13]), sum([25,28,7,0,10,0,31,0])]))