from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = nums[0]
        sub_max = nums[0]
        for n in nums[1:]:
            sub_max = max(sub_max+n, n)

            if sub_max > ans:
                ans = sub_max
        return ans

if __name__ == "__main__":
    sol = Solution()
    print(sol.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))

