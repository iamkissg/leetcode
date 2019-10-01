from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        '''
        题目的要求是非连续的...
        '''
        if not nums:
            return 0

        counter = [1 for _ in range(len(nums))]
        for i in range(1, len(nums)):
            tmp = []
            for j in range(i):
                if nums[j] < nums[i]:
                    tmp.append(counter[j])
            counter[i] = 1 + (0 if not tmp else (max(tmp)))
        return max(counter)


if __name__ == "__main__":
    sol = Solution()
    print(sol.lengthOfLIS([10,9,2,5,3,7,101,18]))