class TreeNode:

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution:
    def numTrees(self, n: int) -> int:
        nums = [i for i in range(1, n+1)]

        self.memo = {}
        n_BST = self.helper(nums)
        return n_BST
    
    def helper(self, nums):
        
        hash = str(nums)
        if hash in self.memo:
            return self.memo[hash]

        if not nums:
            return 0
        if len(nums) == 1:
            return 1

        result = 0
        for i, n in enumerate(nums):
            left = nums[:i]
            right = nums[i+1:]
            n_left = self.helper(left)
            n_right = self.helper(right)
            if not n_left:
                result += n_right
            elif not n_right:
                result += n_left
            else:
                result += self.helper(left) * self.helper(right)

        self.memo[hash] = result
        return result


if __name__ == "__main__":
    sol = Solution()

    print(sol.numTrees(3))
    print(sol.numTrees(2))