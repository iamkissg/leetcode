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
        
        if matrix[0][0] == target:
            return True

        n_row = len(matrix)
        n_col = len(matrix[0])

        start_row = 0
        end_col = n_col - 1

        while end_col >= 0 and start_row < n_row:
            if matrix[start_row][end_col] == target:
                return True
            elif matrix[start_row][end_col] > target:
                end_col -= 1
            else:
                start_row += 1
        return False


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