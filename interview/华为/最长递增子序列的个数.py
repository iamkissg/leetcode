from typing import List
from itertools import chain
from collections import Counter

class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        if not nums: return 0

        d = [{1: 1} for _ in range(len(nums))]
        len_nums = len(nums)

        for i in range(1, len_nums):
            for j in range(i-1, -1, -1):
                if nums[j] >= nums[i]:
                    continue
                # 因为关心的是最长子序列, 我们只要找出最长的即可
                tmp = max(d[j])
                d[i][tmp+1] = d[i].setdefault(tmp+1, 0) + d[j][tmp]

        # print(d)
        md = {}
        for item in d:
            for k, v in item.items():
                md[k] = md.setdefault(k, 0) + v

        # print(md)
        max_len = max(md)
        return md[max_len]

        


if __name__ == "__main__":
    sol = Solution()
    print(sol.findNumberOfLIS([1,3,5,4,7]))
    print(sol.findNumberOfLIS([2,2,2,2,2]))
    print(sol.findNumberOfLIS([1,2,4,3,5,4,7,2]))