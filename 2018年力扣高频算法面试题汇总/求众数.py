from typing import List

from collections import Counter
from math import floor


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        if not nums:
            return None
        
        counter = Counter(nums)
        val, c = counter.most_common(1)[0]
        if c > floor(len(nums)/2):
            return val
        else:
            return None

    def majorityElement(self, nums: List[int]) -> int:
        '''20190920'''
        if not nums:
            return None

        nums.sort()
        return nums[len(nums)//2]


if __name__ == "__main__":
    sol = Solution()
    print(sol.majorityElement([3, 3, 2]))
    print(sol.majorityElement([2,2,1,1,1,2,2]))