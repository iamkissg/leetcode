from typing import List


class Solution:
    def merge_old(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        老方法, 没想到这么长...
        44 ms	13.7 MB	Python3
        同样没想到的是, 这么高效, 击败了 96.04%
        """
        # def get_nums_end_pos(nums: List[int]):
        #     start = 0
        #     end = len(nums) - 1
        #     mid = (start + end) // 2

        #     while start + 1 != end:
        #         if nums[start] <= nums[mid]:
        #             start = mid
        #             mid = (start + end) // 2
        #         elif nums[mid] <= nums[end]:
        #             end = mid
        #             mid = (start + end) // 2
        #     return start

        if not (nums1 or nums2):
            nums1 = []
        elif nums1 and not nums2:
            nums1
        elif not nums1 and nums2:
            nums1 = nums2

        else:
            len_nums1 = len(nums1)
            # nums1_epos = get_nums_end_pos(nums1)
            nums1_epos = m - 1
            nums2_epos = n - 1
            for i in range(len(nums1)):
                if nums1_epos >= 0 and nums2_epos >= 0:
                    if nums1[nums1_epos] >= nums2[nums2_epos]:
                        nums1[len_nums1-i-1] = nums1[nums1_epos]
                        nums1_epos -= 1
                        continue
                    else:
                        nums1[len_nums1-i-1] = nums2[nums2_epos]
                        nums2_epos -= 1
                        continue
                if nums1_epos < 0:
                    nums1[len_nums1-i-1] = nums2[nums2_epos]
                    nums2_epos -= 1
                    continue
                if nums2_epos < 0:
                    nums1[len_nums1-i-1] = nums1[nums1_epos]
                    nums1_epos -= 1
                    continue
        
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        '''
        20191021

        52 ms	13.7 MB	Python3
        '''
        if not nums1:
            return nums2
        if not nums2:
            return nums1

        p1 = m - 1
        p2 = n - 1
        p = len(nums1) - 1

        while p2 >= 0 and p1 >= 0:
            if nums1[p1] < nums2[p2]:
                nums1[p] = nums2[p2]
                p2 -= 1
            else:
                nums1[p] = nums1[p1]
                p1 -= 1
            p -= 1
        else:
            while p2 >= 0:
                nums1[p] = nums2[p2]
                p2 -= 1
                p -= 1        


if __name__ == "__main__":
    sol = Solution()
    # print(sol.merge([], 0, [], 0))
    # print(sol.merge([], 0, [1, 2], 2))
    # print(sol.merge([1, 2], 2, [], 0))
    print(sol.merge([1, 2, 0, 0], 2, [0, 1], 2))