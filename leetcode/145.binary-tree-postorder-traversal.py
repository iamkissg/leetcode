from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
#     def postorderTraversal(self, root: TreeNode) -> List[int]:
#         if not root:
#             return []
        
#         return self.postorderTraversal(root.left) + self.postorderTraversal(root.right) + [root.val]

    def postorderTraversal(self, root: TreeNode) -> List[int]:
        '''
        20191009

        使用 stack 来进行树的 DFS
        '''
        if not root:
            return []
        
        result = []
        visited = set()
        myque = [root]
        while myque:
            node = myque.pop()
            
            if not node.left and not node.right:
                result.append(node.val)
                visited.add(node)
                continue
            else:
                if node not in visited:
                    visited.add(node)
                    myque.append(node)
                    if node.right:
                        myque.append(node.right)
                    if node.left:
                        myque.append(node.left)
                else:
                    result.append(node.val)
        return result

#     def postorderTraversal(self, root: TreeNode) -> List[int]:
#         if not root:
#             return []
        
#         return self.postorderTraversal(root.left) + self.postorderTraversal(root.right) + [root.val]

#     def postorderTraversal_iteratively(self, root: TreeNode) -> List[int]:
#         '''
#         20191009

#         48 ms	13.9 MB	Python3
#         使用 stack 来进行树的 DFS
#         '''
#         if not root:
#             return []

#         res = []
#         stack = [root]
#         visited = set()

#         while stack:
#             node = stack.pop()

#             right = node.right
#             left = node.left

#             # 叶节点
#             if not (left or right):
#                 res.append(node.val)
#                 continue
#             # 中间节点, 第二次访问
#             if node in visited:
#                 res.append(node.val)
#                 continue

#             # 非叶节点第一次被遍历到, 用于取出左右节点, 同时自己再次入栈
#             if node not in visited:
#                 visited.add(node)
#                 stack.append(node)
#             if right:
#                 stack.append(right)
#             if left:
#                 stack.append(left)
#         return res


if __name__ == "__main__":
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.left = TreeNode(3)
    
    sol = Solution()
    print(sol.postorderTraversal(root))
    print(sol.postorderTraversal(root))