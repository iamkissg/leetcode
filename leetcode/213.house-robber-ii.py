from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        '''
        20191011
        44 ms	13.7 MB	Python3

        plan_a: 偷 nums[:-1]
        plan_b: 偷 nums[1:]
        '''
        if not nums:
            return 0
        elif len(nums) <= 2:
            return max(nums)
        
        n = len(nums)
        plan_a = [0 for i in range(n)]
        plan_b = [0 for i in range(n)]

        plan_a[1] = nums[0]
        for i, a in enumerate(nums[1: n-1], start=2):
            plan_a[i] = max(plan_a[i-1], plan_a[i-2]+nums[i-1])

        plan_b[1] = nums[1]
        for i, a in enumerate(nums[2: n], start=2):
            plan_b[i] = max(plan_b[i-1], plan_b[i-2]+nums[i])

        return max(plan_a + plan_b)
        


if __name__ == "__main__":
    sol = Solution()
    print(sol.rob([1, 2, 1, 1]))
    print(sol.rob([3, 2, 1, 3]))
    print(sol.rob([1, 2, 3, 1]))
    print(sol.rob([2, 3, 2]))
    print(sol.rob([1, 1]))