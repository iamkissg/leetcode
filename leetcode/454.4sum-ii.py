from typing import List
from collections import Counter

class Solution:
    # def __init__(self):
    #     self.memo_4sum = {}
    #     self.memo_3sum = {}
    #     self.memo_2sum = {}

    # def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
    #     '''
    #     20191020

    #     O(n^4)+备忘录, 时间复杂度还是太高, 超时
    #     '''
    #     if not A:
    #         return 0

    #     res = []
    #     for i, a in enumerate(A):
    #         target = -a
    #         if target not in self.memo_4sum:
    #             tmp = self.threeSumCount(B, C, D, target)
    #             self.memo_4sum[target] = tmp
    #         res.extend([[i]+item for item in self.memo_4sum[target]])

    #     print(res)
    #     return len(res)
    
    # def threeSumCount(self, B: List[int], C: List[int], D: List[int], target: int):
    #     if not B:
    #         return []
        
    #     if target in self.memo_3sum:
    #         return self.memo_3sum[target]
        
    #     res = []
    #     for i, b in enumerate(B):
    #         cur_target = target - b
    #         tmp = self.twoSumCount(C, D, cur_target)
    #         res.extend([[i]+item for item in tmp])
    #     self.memo_3sum[target] = res
    #     return res

    # def twoSumCount(self, C: List[int], D: List[int], target: int):
    #     if not C:
    #         return []

    #     if target in self.memo_2sum:
    #         return self.memo_2sum[target]
        
    #     res = []
    #     for i_c, c in enumerate(C):
    #         for i_d, d in enumerate(D):
    #             if c+d == target:
    #                 res.append([i_c, i_d])
    #     self.memo_2sum[target] = res
    #     return res

    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        '''
        20191020
        328 ms	39 MB	Python3

        在 Leetcode-cn 上看到网友的解析
        1. 暴力解法, O(n^4), 时间复杂度太高
        2. 将 D 放入查找表中, 时间复杂度 O(n^3), 依然太高
        3. 将 C+D 放入查找表中, 时间复杂度 O(n^2), 可以接受了

        以下实现中, 我用了 Counter 来统计每个 C+D 的出现次数, 需要时, 加上该统计次数即可
        '''
        lookup_table = Counter([c+d for c in C for d in D])

        res = 0
        for i_a, a in enumerate(A):
            for i_b, b in enumerate(B):
                if -a-b in lookup_table:
                    res += lookup_table[-a-b]
        return res


if __name__ == "__main__":
    sol = Solution()
    print(sol.fourSumCount([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                           [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                           [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                           [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]))
    print(sol.fourSumCount([0,1,-1],
                           [-1,1,0],
                           [0,0,1],
                           [-1,1,1]))
    print(sol.fourSumCount(A = [ 1, 2],
                           B = [-2,-1],
                           C = [-1, 2],
                           D = [ 0, 2]))