from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
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
        # print(nums1)


if __name__ == "__main__":
    sol = Solution()

    print(sol.merge([1,2,3,0,0,0], 3, [2, 5, 6], 3))
    print(sol.merge([2, 0], 1, [1], 1))

