from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        '''
        20191004
        白璧微瑕
        '''
        if not matrix or not matrix[0]:
            return []

        row, col = len(matrix), len(matrix[0])
        i = 0
        ans = []
        while col > 2*i and row > 2*i:
            aaa = self.go_through(matrix, i, row, col)
            ans.extend(aaa)
            i += 1
        return ans

    def go_through(self, matrix, i, row, col):
        goes = []
        end_col = col-i  # 不包含, 和第一次循环的 len(matrix[0]) 作用类似, 只是加了 i 控制边界
        end_row = row-i  # 不包含, 同上

        # 此处不需要控制边界, 对于矮胖的, 照常走即可, 对于高瘦的, 不动
        for a in range(i, end_col):
            # print('A', i, a, matrix[i][a])
            goes.append(matrix[i][a])

        for a in range(i+1, end_row):
            # print('B', a, col-1, matrix[a][col-1])
            goes.append(matrix[a][col-i-1])

        # 控制边界条件, 对于矮胖或高窄型型的矩阵, col 和 row 不是同步变化的,
        # 但是我们的算法里, 只用了一个 i, 所以需要控制一下 i 的走势
        # 对于矮胖型的, 最后水平走一趟即可; 对于高瘦型的, 最后竖直走一趟即可,
        # 前面两步已经走过就走了这一步了, 因此下面的循环需要选择性跳过

        # 当前底部, 从右向左遍历, 需要行不重复
        if i+1 < end_row:
            for a in range(end_col-2, i-1, -1):
                # print('C', row-1, a, matrix[row-1][a])
                goes.append(matrix[end_row-1][a])

        # 当前左侧, 从下向上遍历, 需要列不重复
        if i+1 < end_col:
            for a in range(end_row-2, i, -1):
                # print('D', a, i, matrix[a][i])
                goes.append(matrix[a][i])

        return goes


if __name__ == "__main__":
    sol = Solution()
    print(sol.spiralOrder([
        [ 1, 2, 3 ],
        [ 4, 5, 6 ],
        [ 7, 8, 9 ]
    ]))

    print(sol.spiralOrder([
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9,10,11,12]
    ]))
    # [1,2,3,4,8,12,11,10,9,5,6,7]