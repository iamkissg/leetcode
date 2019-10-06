from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        '''
        20191005
        80 ms	16 MB	Python3
        感觉是自己真正意义上写出来的 dp table!!!
        中间走了不少弯路, 尝试过不同的乘积组合, 屡错屡改, 最后还是返璞归真, 使用了比较朴素的判断

        '''
        if not nums:
            return 0

        n = len(nums)
        dp = [[None, None] for _ in range(n)]
        dp[0] = [nums[0], nums[0]]
        for i in range(1, n):
            pre_min, pre_max = dp[i-1][1], dp[i-1][0]

            if nums[i] == 0:
                dp[i][0], dp[i][1] = 0, 0

            elif nums[i] > 0:
                dp[i][0] = max(nums[i], nums[i]*pre_max)
                dp[i][1] = min(nums[i], nums[i]*pre_min)

            elif nums[i] < 0:
                dp[i][0] = max(nums[i], nums[i]*pre_min)
                dp[i][1] = min(nums[i], nums[i]*pre_max)

        return max(item[0] for item in dp)



if __name__ == "__main__":
    sol = Solution()
    print(sol.maxProduct([2,-3,0,1,-2,-3,-1]))
    print(sol.maxProduct([1,0,-1,2,3,-5,-2]))
    print(sol.maxProduct([2,3,-2,4]))
    print(sol.maxProduct([2,3,-2,-1]))
    print(sol.maxProduct([0,2]))
    print(sol.maxProduct([-2,0,-1]))
