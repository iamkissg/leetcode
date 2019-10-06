from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) <= 2:
            return max(nums)

        dp = [0, nums[0]]
        for i, n in enumerate(nums[1:], start=2):
            dp.append(max(dp[i-2]+n, dp[i-1]))

        return max(dp)


if __name__ == "__main__":
    sol = Solution()
    print(sol.rob([2, 1, 1, 2]))
    print(sol.rob([2, 1, 1, 1, 2]))
    print(sol.rob([1,2,3,1]))
    print(sol.rob([2,7,9,3,1]))