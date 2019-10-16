from typing import List
from itertools import combinations


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        res = [[]]
        for a in nums:
            res = res + [item+[a] for item in res]
        return res

if __name__ == "__main__":
    sol = Solution()
    print(sol.subsets([1, 2, 3]))
    print(sol.subsets([1, 2]))
    print(sol.subsets([]))