from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        '''
        20191009
        80 ms	15.1 MB	Python3  # 不判空
        76 ms	15 MB	Python3  # 先判空

        网友的解法:
        https://leetcode-cn.com/problems/longest-consecutive-sequence/solution/dong-tai-gui-hua-python-ti-jie-by-jalan/
        这个思路太巧妙了, 维护了一张字典(哈希表), 然后遍历数组, 如果元素不再字典中, 就将它加入哈希表中, 并做一些更新
        巧妙的地方在于, 每次都更新边界值, 这样如果字典中已有 [1, 3], 增加 2 的时候, 会通过 2 把两边的数组都串起来, 构成一个更长的连续子序列, 然后边界值同时得到更新
        之后不管是在左边界还是右边解增加元素, 都自然地取得了两边可取得的最长子序列长度, amazing
        '''
        if not nums:
            return 0

        d = {}
        max_len = 0
        for a in nums:
            if a not in d:
                l_len = d.get(a-1, 0)
                r_len = d.get(a+1, 0)

                cur_len = 1 + l_len + r_len
                if cur_len > max_len:
                    max_len = cur_len

                d[a] = cur_len
                d[a-l_len] = cur_len
                d[a+r_len] = cur_len

        return max_len

    def longestConsecutive_sort(self, nums: List[int]) -> int:
        '''
        20191009
        76 ms	14.7 MB	Python3

        有点意外， 讲道理， 先 sort 会有一个 O(nlogn) 的时间开销, 没想到用时一样
        '''
        if not nums:
            return 0

        nums.sort()

        cur_len = 1
        max_len = 1
        for r, a in enumerate(nums[1:], start=1):
            diff = nums[r]-nums[r-1]
            if diff == 1:
                cur_len += 1
                max_len = max(max_len, cur_len)
            elif diff == 0:
                continue
            else:
                cur_len = 1
        return max_len

if __name__ == "__main__":
    sol = Solution()
    print(sol.longestConsecutive([0,3,7,2,5,8,4,6,0,1]))
    print(sol.longestConsecutive([100, 1, 200, 4, 2, 3]))
    print(sol.longestConsecutive([100, 4, 200, 1, 3, 2]))
    print(sol.longestConsecutive([]))
    print(sol.longestConsecutive([100]))
    print(sol.longestConsecutive([1,1]))
    print(sol.longestConsecutive([1,2,0,1]))
    print()
    print(sol.longestConsecutive_sort([0,3,7,2,5,8,4,6,0,1]))
    print(sol.longestConsecutive_sort([100, 1, 200, 4, 2, 3]))
    print(sol.longestConsecutive_sort([100, 4, 200, 1, 3, 2]))
    print(sol.longestConsecutive_sort([]))
    print(sol.longestConsecutive_sort([100]))
    print(sol.longestConsecutive_sort([1,1]))
    print(sol.longestConsecutive_sort([1,2,0,1]))