from typing import List
from itertools import combinations

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        mi = []
        for i in range(n+1):
            mi.extend(combinations(nums, i))
        return list(map(list, mi))


if __name__ == "__main__":
    sol = Solution()
    print(sol.subsets([1, 2, 3]))
