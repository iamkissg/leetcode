from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if not nums:
            return None
        if len(nums) == 1:
            return TreeNode(nums[0])
        else:
            mid_pos = len(nums) // 2
            tn = TreeNode(nums[mid_pos])
            tn.left = self.sortedArrayToBST(nums[:mid_pos])
            tn.right = self.sortedArrayToBST(nums[mid_pos+1:])
            return tn


if __name__ == "__main__":
    sol = Solution()
    tn = sol.sortedArrayToBST([-10, -3, 0, 5, 9])
    print(tn)