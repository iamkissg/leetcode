from typing import List


v_opts = [-1, -1, -1, 0, 0, 1, 1, 1]
h_opts = [-1, 0, 1, -1, 1, -1, 0, 1]


class Solution:

    def searchAround(self, board, i, j, v_length, h_length):

        count = 0
        for v, h in zip(v_opts, h_opts):
            if 0<=i-v<v_length and 0<=j-h<h_length:
                if board[i-v][j-h] == 1:
                    count += 1
        return count


    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        v_length = len(board)
        h_length = len(board[0])

        counter = {
            (i, j): (board[i][j], self.searchAround(board, i, j, v_length, h_length))
            for i in range(v_length) for j in range(h_length)
        }
        for i in range(v_length):
            for j in range(h_length):
                if counter[(i, j)][0] == 0 and counter[(i, j)][1] == 3:
                    board[i][j] = 1
                elif counter[(i, j)][0] == 1 and counter[(i, j)][1] < 2:
                    board[i][j] = 0
                elif counter[(i, j)][0] == 1 and counter[(i, j)][1] in {2, 3}:
                    continue
                elif counter[(i, j)][0] == 1 and counter[(i, j)][1] > 3:
                    board[i][j] = 0

        for row in board:
            print(row)
        # return board

if __name__ == "__main__":
    sol = Solution()
    print(sol.gameOfLife([[0,1,0],
                          [0,0,1],
                          [1,1,1],
                          [0,0,0]]))
                
        