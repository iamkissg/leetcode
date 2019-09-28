from typing import List

'''
20190928

根据 leetcode-cn 上题解一边看一边学写的,
初看很难, 但对问题进行下分类, 抽丝剥茧地看, 问题就清晰了, 会看上去不那么难
当 k == 1 的时候, 问题就退化为最大子序列和问题
当 k == 2 时, 因为拼接的关系, 会存在最大前缀和最大后缀, 就变成求最大前后缀和与最大子序列和哪一个更大
当 k > 2 时, 要看整个序列的和是否大于0, 如果是, 那么第一个用最大后缀, 最后一个用最大前缀, 中间的用整个序列, 如此求得的就是最大值
                                   如果不是, 问题退化为 k==2 的情况, 或者将中间的序列看作 0.
'''

class Solution:
    MOD = 10**9 + 7

    def kConcatenationMaxSum(self, arr: List[int], k: int) -> int:
        sub_arr_max = [0]

        for n in arr:
            if sub_arr_max[-1] >= 0:
                sub_arr_max.append(sub_arr_max[-1]+n)
            else:
                sub_arr_max.append(n)
        arr_max = max(sub_arr_max)
        if k == 1:
            return arr_max % self.MOD

        # 很费事的运算, 写出来就是傻
        # pre_max = max([sum(arr[:i]) for i in range(len(arr)+1)])
        # suf_max = max([sum(arr[i:]) for i in range(len(arr))])

        pre_sum = 0
        suf_sum = 0
        pre_max = 0
        suf_max = 0

        len_arr = len(arr)
        for i in range(len_arr):
            pre_sum += arr[i]
            suf_sum += arr[len_arr-1-i]
            if pre_sum > pre_max:
                pre_max = pre_sum
            if suf_sum > suf_max:
                suf_max = suf_sum
        
        arr_sum = sum(arr)
        cat_max = max(0, pre_max + suf_max + (arr_sum if arr_sum >= 0 else 0) * (k-2)) % self.MOD
        return max(cat_max, arr_max)


if __name__ == "__main__":
    sol = Solution()
    # print(sol.kConcatenationMaxSum(arr = [1,2], k = 3))
    # print(sol.kConcatenationMaxSum(arr = [1,-2,1], k = 5))
    # print(sol.kConcatenationMaxSum(arr = [1,-1], k = 2))
    # print(sol.kConcatenationMaxSum(arr = [1,-1], k = 1))
    print(sol.kConcatenationMaxSum(arr = [1,0,4,1,4], k = 4))