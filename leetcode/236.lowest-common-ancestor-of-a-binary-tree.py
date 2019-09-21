# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        '''
        20190921
        常规解法, 适用于一般二叉树, 同样来自覃超的算法课
        在子树中查找 p 和 q, 如果 p 或 q 正好为 root, 那就是它们的最近公共祖先了
        否则的话, 有 3 种情况, pq 在左子树中, pq 在右子树中, pq 分别在左右子树中
        1. pq 在左子树中, 那么在右子树中找不到, 返回 None
        2. 同 1
        3. 在两颗子树中都找到了 p 或 q, root 就是最近的公共祖先

        执行用时 :100 ms, 在所有 Python3 提交中击败了95.53% 的用户
        '''
        if root is None or root == p or root == q:
            return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        
        if left is not None and right is not None:
            return root
        else:
            if right is None:
                return left
            else:
                return right
