from typing import List

from functools import reduce


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return reduce(lambda x, y: x^y, nums)


if __name__ == "__main__":
    sol = Solution()
    print(sol.singleNumber([2,2,1]))
    print(sol.singleNumber([4,1,2,1,2]))
        