from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows < 0:
            raise ValueError
        elif numRows == 0:
            return []
        elif numRows == 1:
            return [[1]]
        else:
            L = [[1], [1, 1]]
            for i in range(2, numRows):
                pre_l = L[-1]
                l = [1]
                for a, b in zip(pre_l[:-1], pre_l[1:]):
                    l.append(a+b)
                L.append(l+[1])
            return L


if __name__ == "__main__":
    sol = Solution()
    print(sol.generate(5))
    print(sol.generate(6))
    print(sol.generate(7))