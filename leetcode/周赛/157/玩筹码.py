from typing import List


class Solution:
    def minCostToMoveChips(self, chips: List[int]) -> int:
        evens = [c for c in chips if not c&1]
        odds = [c for c in chips if c&1]
        return min(len(evens), len(odds))


        


if __name__ == "__main__":
    sol = Solution()
    print(sol.minCostToMoveChips([1,2,3]))
    print(sol.minCostToMoveChips([1,2,2,2,2]))
    print(sol.minCostToMoveChips([2,2,2,3,3]))
    print(sol.minCostToMoveChips([2,2,2,2,4]))
    print(sol.minCostToMoveChips([1,2,3,4,5,6]))