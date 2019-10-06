from typing import List
from sys import maxsize

INT_MIN = -maxsize

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0

        max_sum = INT_MIN
        sub_sum = INT_MIN
        for n in nums:
            sub_sum = max(sub_sum+n, n)
            if sub_sum > max_sum:
                max_sum = sub_sum
        return max_sum


if __name__ == "__main__":
    sol = Solution()
    print(sol.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))