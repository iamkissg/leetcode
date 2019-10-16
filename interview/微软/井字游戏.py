from typing import List
from collections import Counter


class Solution:
    def validTicTacToe(self, board: List[str]) -> bool:
        mat = [list(row) for row in board]
        counter = Counter((item for row in mat for item in row))
        counter.setdefault('X', 0)
        counter.setdefault('O', 0)
        diff_X_O = counter['X'] - counter['O']
        total = counter['X'] + counter['O']
        if diff_X_O < 0 or diff_X_O > 1 :
            return False
        mat_T = [col for col in zip(*mat)]

        # for row in mat:
        #     print(row)
        # print('#'*10)
        # for row in mat_T:
        #     print(row)

        win = 0
        for i in range(3):
            if len(set(mat[i])) == 1 and mat[i][0] == 'X':
                if win and total < 9:
                    return False
                if counter['X'] == counter['O']:
                    return False
                win += 1
            if len(set(mat_T[i])) == 1 and mat_T[i][0] 'X':
                if win and total < 9:
                    return False
                win += 1

        diag_1 = [mat[0][0], mat[1][1], mat[2][2]]
        diag_2 = [mat[0][2], mat_T[1][1], mat[2][0]]
        if len(set(diag_1)) == 1 and diag_1[0] in {'X', 'O'}:
                if win and total < 9:
                    return False
                win += 1
        if len(set(diag_2)) == 1 and diag_2[0] in {'X', 'O'}:
                if win and total < 9:
                    return False
                win += 1

        return True



if __name__ == "__main__":
    sol = Solution()
    print(sol.validTicTacToe(board = ["XXX","XOO","OO "]))
    print(sol.validTicTacToe(board = ["XXX","OOX","OOX"]))
    print(sol.validTicTacToe(board = ["O  ", "   ", "   "]))
    print(sol.validTicTacToe(board = ["XOX", " X ", "   "]))
    print(sol.validTicTacToe(board = ["XXX", "   ", "OOO"]))
    print(sol.validTicTacToe(board = ["XOX", "O O", "XOX"]))