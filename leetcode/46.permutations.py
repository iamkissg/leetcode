from typing import List
from itertools import permutations


class Solution:
    # def permute(self, nums: List[int]) -> List[List[int]]:
    #     return permutations(nums, len(nums))

    def permute(self, nums: List[int]) -> List[List[int]]:
        return self.helper(nums)

    def helper(self, nums):
        if not nums:
            return [[]]
        if len(nums) == 1:
            return [nums]

        return [[n]+pm for i, n in enumerate(nums) for pm in self.helper(nums[:i]+nums[i+1:])]


if __name__ == "__main__":
    sol = Solution()
    print(sol.permute([1,2,3]))
    print(sol.permute([]))
    print(sol.permute([1]))