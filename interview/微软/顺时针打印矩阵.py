from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return []

        n_row, n_col = len(matrix), len(matrix[0])

        start = 0
        res = []
        while n_row > 2*start and n_col > 2*start:
            res.extend(self.oneCircle(matrix, start, n_row, n_col))
            start += 1

        return res
        
    def oneCircle(self, matrix: List[List[int]], start, n_row, n_col):
        res = []
        end_row = n_row-start-1  # [start, end_row]
        end_col = n_col-start-1  # [start, end_col]

        for col in range(start, end_col+1):
            res.append(matrix[start][col])

        for row in range(start+1, end_row+1):
            res.append(matrix[row][end_col])

        # 条件判断: 高瘦和矮胖型的矩阵, 不必再跑一趟, 

        if start < end_row:
            for col in range(end_col-1, start-1, -1):
                res.append(matrix[end_row][col])

        if start < end_col:
            for row in range(end_row-1, start, -1):
                res.append(matrix[row][start])

        return res

if __name__ == "__main__":
    sol = Solution()
    print(sol.spiralOrder([
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9,10,11,12]
    ]))
    print(sol.oneCircle([
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9,10,11,12]
    ], 0, 3, 4))
    print(sol.oneCircle([
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9,10,11,12]
    ], 1, 3, 4))