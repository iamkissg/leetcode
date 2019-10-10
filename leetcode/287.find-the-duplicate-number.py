from typing import List
from functools import reduce
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        '''
        20191009

        题目要求:
            - 不能更改原数组（假设数组是只读的）  # 不能使用原地排序算法
            - 只能使用额外的 O(1) 的空间       # 非原地排序算法也不行
            - 时间复杂度小于 O(n2)            # 不能有两重循环
            - 数组中只有一个重复的数字，但它可能不止重复出现一次。  # 一个重复数字, 出现两次以上
        数组可能很大很大很大很大

        复现这位网友的"二分"思路, 也是精妙啊
        https://leetcode-cn.com/problems/find-the-duplicate-number/solution/er-fen-fa-si-lu-ji-dai-ma-python-by-liweiwei1419/
        根据题目的特性, 因为 1+n 大小的数组, 每个元素值在 1~n 之间,
        用二分的思想, 找到中间值元素, 如果有一半的元素大于中间值, 说明重复的数值在比中间值大的那部分 (这是什么神奇的思路)
        如此就构成了二分的思想, 每次可以缩小一半的搜索区间
        
        大概总结一下二分查找的功能:
        1. 搜索有序数组中的某个值
        2. 搜索有序数组中的左右边界
        3. 在近似有序(比如每一行每一列都是有序的二维数组中), 找到某个值的位置
        4. (本题) 查找一定范围内查找唯一的重复元素

        '''
        
        l = 1
        n = len(nums)
        r = n - 1
        while l < r:
            mid = (l+r+1) >> 1
            # count = sum([1 if a < mid else 0 for a in nums])
            count = 0
            for a in nums:
                if a < mid:
                    count += 1

            if count >= mid:
                r = mid - 1
            elif count < mid:
                l = mid

        return l


if __name__ == "__main__":
    sol = Solution()
    print(sol.findDuplicate([1,3,4,2,2,2]))
    print(sol.findDuplicate([1,3,4,2,2]))
    print(sol.findDuplicate([3,1,3,4,2]))
    print(sol.findDuplicate([1,1,3,4,2]))
    print(sol.findDuplicate([4,1,3,4,2]))
    print(sol.findDuplicate([3,3,1,2]))