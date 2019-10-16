from typing import List


class Solution:
    def longestLine(self, M: List[List[int]]) -> int:
        if not M or not M[0]:
            return 0

        # dx = [-1, -1, -1, 0, 0, 1, 1, 1]
        # dy = [-1, 0, 1, -1, 1, -1, 0, 1]
        step = [(-1, 1), (0, -1), (-1, 0), (-1, -1)]

        n, m = len(M), len(M[0])
        new_M = [[0] * (m+2)]
        for row in M:
            new_M.append([0]+row+[0])
        new_M.append([0] * (m+2))

        for row in M:
            print(row)
        for row in new_M:
            print(row)

        # 主对角线, 横, 竖, 反对角线
        dp = [[[0 for _ in range(4)] for _ in range(m+2)] for _ in range(n+2)]
        max_len = 0
        for i in range(1, n+1):
            for j in range(1, m+1):
                if new_M[i][j] == 1:
                    print(i, j)
                    dp[i][j][0] = dp[i+step[0][0]][j+step[0][1]][0]+1
                    dp[i][j][1] = dp[i+step[1][0]][j+step[1][1]][1]+1
                    dp[i][j][2] = dp[i+step[2][0]][j+step[2][1]][2]+1
                    dp[i][j][3] = dp[i+step[3][0]][j+step[3][1]][3]+1
                    max_len = max(max_len, dp[i][j][0], dp[i][j][1], dp[i][j][2], dp[i][j][3])

        return max_len

if __name__ == "__main__":
    sol = Solution()
    print(sol.longestLine([
        [0,1,1,0],
        [0,1,1,0],
        [0,0,0,1]
    ]))