from typing import List
from collections import Counter


class Solution:
    # def findDuplicates(self, nums: List[int]) -> List[int]:
    #     '''
    #     执行用时 :416 ms
    #     内存消耗 :22.2 MB
    #     '''
    #     if not nums:
    #         return []

        # return [k for k, v in Counter(nums).items() if v == 2]


    def findDuplicates(self, nums: List[int]) -> List[int]:
        if not nums:
            return []

        ans = []
        for i in range(len(nums)):
            popped = nums.pop()
            if popped in nums:
                ans.append(popped)
        return ans

if __name__ == "__main__":
    sol = Solution()
    print(sol.findDuplicates([4,3,2,7,8,2,3,1]))