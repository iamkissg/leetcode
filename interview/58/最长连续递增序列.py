from typing import List


class Solution:
    # def findLengthOfLCIS(self, nums: List[int]) -> int:
    #     '''
    #     20191013
    #     该方法求的是最长递增子序列, 但是不满足题目中的*连续*要求
    #     '''
    #     if not nums:
    #         return 0

    #     n = len(nums)
    #     dp = [1 for _ in range(n)]

    #     for i, a in enumerate(nums[1:], start=1):
    #         dp[i] = max([dp[j] for j, b in enumerate(nums[:i]) if a > b]+[0]) + 1
    #     return max(dp)

    def findLengthOfLCIS(self, nums: List[int]) -> int:
        '''
        20191013
        感觉要求连续比不要求连续更简单
        '''
        if not nums:
            return 0

        n = len(nums)
        cur_len, max_len = 1, 1
        for r in range(1, n):
            if nums[r] > nums[r-1]:
                cur_len += 1
                if cur_len > max_len:
                    max_len = cur_len
            else:
                cur_len = 1

        return max_len

if __name__ == "__main__":
    sol = Solution()
    print(sol.findLengthOfLCIS( [1,3,5,4,7]))
    print(sol.findLengthOfLCIS( [2, 2, 2, 2, 2]))