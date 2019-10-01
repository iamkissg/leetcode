from typing import List
from math import factorial


class Solution:
    def Cn2(self, n):
        return n*(n-1)//2

    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        unique_dominoes = {}
        for d in dominoes:
            td = tuple(sorted(d))
            if td not in unique_dominoes:
                unique_dominoes[td] = 0
            unique_dominoes[td] += 1

        result = sum(self.Cn2(v) for v in unique_dominoes.values() if v > 1)
        return result

if __name__ == "__main__":
    sol = Solution()
    print(sol.numEquivDominoPairs(dominoes = [[1,2],[2,1],[3,4],[5,6]]))
    print(sol.numEquivDominoPairs(dominoes = [[1,2],[2,1],[3,4],[4, 3]]))
    print(sol.numEquivDominoPairs(dominoes = [[1,2],[1,2],[1,1],[1,2],[2,2]]))