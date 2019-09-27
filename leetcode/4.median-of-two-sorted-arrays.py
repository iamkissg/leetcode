from typing import List
import sys

INT_MAX = sys.maxsize  
INT_MIN = -sys.maxsize-1


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        '''
        20190926
        执行用时 :112 ms, 在所有 Python3 提交中击败了79.95% 的用户
        内存消耗 :13.8 MB, 在所有 Python3 提交中击败了5.28%的用户

        自己做不出来, 看了网友的解法很久, 依然一知半解, 先敲出来, 跑一遍再说
        从中位数的定义出发, 所谓中位数, 就是对一个有序数组, 在这个数左边的数的数量等于它右边的数的数量
        因此, 找出两个有序数组的中位数, 就是要找到一个数, 使得两个数字中在这个数左边的数的总数占数组容量的一半
        暴力解法可以是, 从两个数字的第一个元素开始, 一步步往后移动, 直到划过两个数组容量一半的数字
        题设要求, O(log(n+m)) 的时间复杂度, 看到 log + 有序数组, 自然地想到二分查找
        1. 为了简化操作, 可以将第一个数组固定为较短的那个, 然后对它进行划分, 可以得到左右两部分,
        2. 在已经知道中位数左边有多少个数字的情况下, 易得第二个数组的划分位置,
        3. 如此不断地调整第一个划分的位置, 就能找到最终中位数的位置

        此时可以遇到第一个数组中的数字全部大于或者小于中位数的情况, 要在第二个数组中找到中位数比较容易

        该解法中用了一个小技巧, 就是抽象了两个虚拟数组, 从而将数组长度和需要分奇偶的情况简化一种情况
        '''
        if len(nums1) > len(nums2):
            # 保证 nums1 是比较短的那个, 方便操作
            return self.findMedianSortedArrays(nums2, nums1)

        n, m = len(nums1), len(nums2)
        # hi 取 2n, 是因为抽象了虚拟数组, 假设每个数字前都填充了一个空位, 此时, 2n 就对应第一个虚拟数组中最后一个数字后的位置 (最后一个数字的索引为 2n-1)
        # lo 取 0, 在虚拟数组中对应第一个空位的索引, 但是只要 lo//2, 其实依然为0, 是第一个数字在原数组中的索引, 没关系
        lo, hi = 0, 2*n  
        
        while lo <= hi:
            c1 = (lo+hi) // 2  # 第一个虚拟数组的划分点
            c2 = m+n-c1        # 涉及到虚拟数组, 所以 m+n-c1 即可

            # 自然划分的情况下, lmax1 < rmax1, lmax2 < rmin2, 而中位数需要满足将两个数组都分成了两个部分, 所以需要满足 lmax1 < rmin2, lmax2 < rmin1
            # 极端情况下, 第一个数组的数字都大于中位数, 为了使 lmax1<rmin2, 直接给 lmax1 赋全局最小值
            # else 之后的语句是从虚拟数组中直接计算原数组中对应位置的数字, 是一个 trick
            lmax1 = INT_MIN if c1 == 0 else nums1[(c1-1)//2]
            # 极端情况下, 第一个数组的数字都小于中位数, 为了使 lmax2<rmin1, 直接给 rmin1 赋全局最大值
            rmin1 = INT_MAX if c1 == 2*n else nums1[c1//2]
            # 类似上述情况
            lmax2 = INT_MIN if c2 == 0 else nums2[(c2-1)//2]
            rmin2 = INT_MAX if c2 == 2*m else nums2[c2//2]

            if lmax1 > rmin2:
                hi = c1-1
            elif lmax2 > rmin1:
                lo = c1+1
            else:
                break

        return (max(lmax1, lmax2) + min(rmin1, rmin2))/2


if __name__ == "__main__":
    sol = Solution()
    print(sol.findMedianSortedArrays(
        nums1 = [1, 3],
        nums2 = [2]
    ))
    print(sol.findMedianSortedArrays(
        nums1 = [1, 2],
        nums2 = [3, 4]
    ))
