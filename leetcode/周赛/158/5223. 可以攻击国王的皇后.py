from typing import List


class Solution:

    dx = [-1, -1, -1, 0, 0, 1, 1, 1]
    dy = [-1, 0, 1, -1, 1, -1, 0, 1]
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:

        king_x = king[0]
        king_y = king[1]
        queens_set = {tuple(q) for q in queens}

        
        res = []
        for i in range(8):
            step_x, step_y = self.dx[i], self.dy[i]
            x, y = king_x+step_x, king_y+step_y
            while 0<=x<8 and 0<=y<8:
                if (x, y) in queens_set:
                    res.append([x, y])
                    break
                x += step_x
                y += step_y

        return list(res)

if __name__ == "__main__":
    sol = Solution()
    print(sol.queensAttacktheKing(queens = [[0,1],[1,0],[4,0],[0,4],[3,3],[2,4]], king = [0,0]))
    print(sol.queensAttacktheKing(queens = [[0,0],[1,1],[2,2],[3,4],[3,5],[4,4],[4,5]], king = [3,3]))
    print(sol.queensAttacktheKing(queens = [[5,6],[7,7],[2,1],[0,7],[1,6],[5,1],[3,7],[0,3],[4,0],[1,2],[6,3],[5,0],[0,4],[2,2],[1,1],[6,4],[5,4],[0,0],[2,6],[4,5],[5,2],[1,4],[7,5],[2,3],[0,5],[4,2],[1,0],[2,7],[0,1],[4,6],[6,1],[0,6],[4,3],[1,7]], king = [3,4]))