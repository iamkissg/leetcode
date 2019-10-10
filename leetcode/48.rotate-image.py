from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.

        20191010
        48 ms	13.8 MB	Python3

        记得从哪里看到过 Python 的 zip 能实现二维矩阵转置, 但是没记住代码, 这就是没深入思考过的毛病
        用 zip 实现二维矩阵的转置, 实际就是通过 zip, 把每一行数组对齐了然后依次取同一位, 就构成了一个按列取元素的数组
        """
        if not matrix or not matrix[0]:
            return [[]]

        # 下面这句是不可行的, 题目要求是原地旋转, 是要对原矩阵进行操作, 下面这个其实是重新创建了一个对象, 赋给 matrix
        # matrix = [row[::-1] for row in zip(*matrix)]
        matrix[:] = [row[::-1] for row in zip(*matrix)]

if __name__ == "__main__":
    sol = Solution()
    print(sol.rotate(matrix = [
      [1,2,3],
      [4,5,6],
      [7,8,9]
    ],))