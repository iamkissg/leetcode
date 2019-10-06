from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return [[1], [1, 1]]
        
        tri = [[1], [1, 1]]
        for _ in range(3, numRows+1):
            last_line = tri[-1]
            cur_line = [1]+[i+j for i, j in zip(last_line[:-1], last_line[1:])]+[1]
            tri.append(cur_line)
        return tri


if __name__ == "__main__":
    sol = Solution()
    print(sol.generate(0))
    print(sol.generate(1))
    print(sol.generate(2))
    print(sol.generate(3))
    print(sol.generate(4))
    print(sol.generate(5))
    print(sol.generate(6))
