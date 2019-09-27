from typing import List
import queue

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrder_DFS(self, root: TreeNode) -> List[List[int]]:
        '''
        20190924
        # 和 BFS 的效率差不离
        执行用时 :48 ms, 在所有 Python3 提交中击败了93.50% 的用户
        内存消耗 :14.8 MB, 在所有 Python3 提交中击败了5.20%的用户
        '''
        if not root:
            return []
        
        # 看过覃超的算法课, 知道 DFS 也可以用来解决本题, 但是印象比较模糊
        # 自己写的话, 比较粗糙地在深度优先遍历的过程中, 带着 result 跑
        # 另外, 要记录一个深度, 不然节点不知道自己处在哪一层的
        result = self.DFS_helper(root, 0, [])
        return result
        
    def DFS_helper(self, root, depth, result):
        if not root:
            return result

        depth += 1
        if len(result) < depth:
            result.append([])
        
        result[depth-1].append(root.val)
        if root.left:
            result = self.DFS_helper(root.left, depth, result)
        if root.right:
            result = self.DFS_helper(root.right, depth, result)
        return result


    def levelOrder_BFS(self, root: TreeNode) -> List[List[int]]:
        '''
        20190924
        执行用时 :44 ms, 在所有 Python3 提交中击败了98.24% 的用户
        内存消耗 :14.3 MB, 在所有 Python3 提交中击败了5.20%的用户
        '''
        if not root:
            return []

        # 广度优先遍历对图有用, 对树没用
        # visited = set()

        my_queue = queue.deque([root])
        result = []
        while my_queue:
            # 这一点很巧妙, 用了一个内循环来控制层数, 来自覃超的算法课
            layer_size = len(my_queue)
            result.append([])

            for n in range(layer_size):
                node = my_queue.popleft()
                result[-1].append(node.val)

                if node.left:
                    my_queue.append(node.left)
                if node.right:
                    my_queue.append(node.right)
        return result

    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        return self.levelOrder_BFS(root)

if __name__ == "__main__":
    sol = Solution()

    root = TreeNode(2)
    root.left = TreeNode(3)
    root.right = TreeNode(89)
    root.right.left = TreeNode(8)
    root.right.right = TreeNode(9)

    print(sol.levelOrder(root))
    print(sol.levelOrder_DFS(root))