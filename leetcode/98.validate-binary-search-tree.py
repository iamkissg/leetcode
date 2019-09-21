# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def inorder(self, root):
        if not root:
            return []
        return self.inorder(root.left) + [root.val] + self.inorder(root.right)

    def isValidBST(self, root: TreeNode) -> bool:
        '''
        20190921
        根据二叉搜索树的特点来, 按照中序遍历, 将得到一个严格有序的数组
        68 ms	17.5 MB	Python3
        '''
        arr = self.inorder(root)
        return len(set(arr)) == len(arr) and sorted(arr) == arr


    def isValidBST2(self, root: TreeNode) -> bool:
        '''
        20190921
        解法来自覃超的算法课, 直接遍历树(中序)
        按照二叉搜索树的性质, 当前节点要比前继节点大
        52 ms	16.5 MB	Python3
        '''
        self.prev = None
        return self.inorder_traverse(root)


    def inorder_traverse(self, root):
        if root is None:
            return True
        if not self.inorder_traverse(root.left):
            return False
        if self.prev and self.prev.val >= root.val:
            return False
        self.prev = root
        return self.inorder_traverse(root.right)


if __name__ == "__main__":
    sol = Solution()

    my_tree = TreeNode(2)
    my_tree.left = TreeNode(1)
    my_tree.right = TreeNode(3)
    print(sol.isValidBST2(my_tree))