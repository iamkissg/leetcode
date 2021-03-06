from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []

        return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)

    def inorderTraversal_iteratively(self, root: TreeNode) -> List[int]:
        '''
        20191009
        40 ms	13.8 MB	Python3

        使用 stack 来进行树的 DFS
        '''
        if not root:
            return []

        res = []
        stack = [root]
        visited = set()

        while stack:
            node = stack.pop()
            if not node:
                continue

            right = node.right
            left = node.left

            # 叶节点
            if not (left or right):
                res.append(node.val)
                continue
            # 中间节点, 第二次访问
            if node in visited:
                res.append(node.val)
                continue

            if right:
                stack.append(right)
            # 非叶节点第一次被遍历到, 用于取出左右节点, 同时自己再次入栈
            if node not in visited:
                visited.add(node)
                stack.append(node)
            if left:
                stack.append(left)
        return res


if __name__ == "__main__":
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.left = TreeNode(3)
    
    sol = Solution()
    print(sol.inorderTraversal(root))
    print(sol.inorderTraversal_iteratively(root))