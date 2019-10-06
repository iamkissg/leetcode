from typing import List
from itertools import combinations

class Solution:
    # def subsets(self, nums: List[int]) -> List[List[int]]:
    #     '''
    #     20191005
    #     40 ms	13.9 MB	Python3
    #     '''
    #     n = len(nums)
    #     mi = []
    #     for i in range(n+1):
    #         mi.extend(combinations(nums, i))
    #     return list(map(list, mi))

    def subsets(self, nums: List[int]) -> List[List[int]]:
        '''
        20191005

        https://leetcode-cn.com/problems/subsets/solution/hui-su-suan-fa-by-powcai-5/
        网友的代码, 太漂亮了
        '''
        mi = [[]]
        for i in nums:
            mi = mi + [[i] + num for num in mi]
        return mi


if __name__ == "__main__":
    sol = Solution()
    print(sol.subsets([1, 2, 3]))
