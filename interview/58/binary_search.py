from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)

        l, r = 0, n-1
        while l <= r:
            # 右移是有问题的, 会导致死循环
            # mid = l + (r-l)>>1
            mid = l + (r-l)//2
            if nums[mid] < target:
                l = mid+1
            elif nums[mid] > target:
                r = mid-1
            else:
                return mid
        else:
            return -1

if __name__ == "__main__":
    sol = Solution()
    print(sol.search(nums = [-1,0,3,5,9,12], target = 9))