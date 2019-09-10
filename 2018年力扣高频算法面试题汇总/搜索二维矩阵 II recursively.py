class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix:
            return False
        elif not matrix[0]:
            return False
        
        n_row = len(matrix)
        n_col = len(matrix[0])

        if matrix[0][n_col-1] == target:
            return True
        elif matrix[0][n_col-1] < target:
            return self.searchMatrix(matrix[1:], target)
        else:
            return self.searchMatrix([m[:n_col-1] for m in matrix], target)


if __name__ == "__main__":
    sol = Solution()

    print(sol.searchMatrix([
        [1,   4,  7, 11, 15],
        [2,   5,  8, 12, 19],
        [3,   6,  9, 16, 22],
        [10, 13, 14, 17, 24],
        [18, 21, 23, 26, 30]
    ], 5))

    print(sol.searchMatrix([
        [1,   4,  7, 11, 15],
        [2,   5,  8, 12, 19],
        [3,   6,  9, 16, 22],
        [10, 13, 14, 17, 24],
        [18, 21, 23, 26, 30]
    ], 20))

    print(sol.searchMatrix([[]], 20))

    print(sol.searchMatrix([[-1], [-1]], -2))