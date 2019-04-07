from typing import List


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex < 0:
            raise ValueError
        elif rowIndex == 0:
            return [1]
        elif rowIndex == 1:
            return [1, 1]
        else:
            L = [[1], [1, 1]]
            for i in range(rowIndex-1):
                pre_l = L[-1]
                l = [1]
                for a, b in zip(pre_l[:-1], pre_l[1:]):
                    l.append(a+b)
                L.append(l+[1])
            return l+[1]


if __name__ == "__main__":
    sol = Solution()
    print(sol.generate(3))
    print(sol.generate(5))
    print(sol.generate(6))
    print(sol.generate(7))