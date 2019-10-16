from typing import List


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        '''
        20191015

        最先直观的思路: 递归回溯
        我离成功就差一步, 就差一步记忆化啊啊啊啊啊啊, 因为我在递归的过程中, 其实已经找到了某个位置的最长序列,
        那么, 以后搜索到该位置, 可以直接用这个序列即可, 感觉自己菜成狗
        '''
        if not matrix or not matrix[0]:
            return 0
        
        self.memo = {}
        
        results = []
        n, m = len(matrix), len(matrix[0])
        for i in range(n):
            for j in range(m):
                results.append(self.dfs_LIP(matrix, [i, j], n, m))
        return len(max(results, key=len))

    def dfs_LIP(self, mat, cur_path, n, m):
        hash = tuple(cur_path)
        if hash in self.memo:
            return self.memo[hash]

        dx = [-1, 0, 0, 1]
        dy = [0, -1, 1, 0]
        i, j = cur_path
        continued_paths = []
        for step in range(4):
            new_i, new_j = i+dx[step], j+dy[step]
            if new_i < 0 or new_i >= n or new_j < 0 or new_j >= m:
                continue
            if mat[new_i][new_j] <= mat[i][j]:
                continue
            continued_paths.append(self.dfs_LIP(mat, [new_i, new_j], n, m))
        if continued_paths:
            self.memo[hash] = [cur_path] + sorted(continued_paths, key=len, reverse=True)[0]
            return self.memo[hash]
        else:
            return [cur_path]

if __name__ == "__main__":
    sol = Solution()
    # 我不知道为什么会有这么奇葩的输入, 不是矩阵吗
    print(sol.longestIncreasingPath([
        [0,1,2,3,4,5,6,7,8,9],
        [19,18,17,16,15,14,13,12,11,10],
        [20,21,22,23,24,25,26,27,28,29],
        [39,38,37,36,35,34,33,32,31,30],
        [40,41,42,43,44,45,46,47,48,49],
        [59,58,57,56,55,54,53,52,51,50],
        [60,61,62,63,64,65,66,67,68,69],
        [79,78,77,76,75,74,73,72,71,70],
        [80,81,82,83,84,85,86,87,88,89],
        [99,98,97,96,95,94,93,92,91,90],
        [100,101,102,103,104,105,106,107,108,109],
        [119,118,117,116,115,114,113,112,111,110],
        [120,121,122,123,124,125,126,127,128,129],
        [139,138,137,136,135,134,133,132,131,130],
        [0,0,0,0,0,0,0,0,0,0]]))
    print(sol.longestIncreasingPath([
        [9,9,4],
        [6,6,8],
        [2,1,1]
    ]))

    print(sol.longestIncreasingPath([
        [3,4,5],
        [3,2,6],
        [2,2,1]
    ] ))