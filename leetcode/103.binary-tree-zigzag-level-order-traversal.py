from typing import List
from queue import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        
        myque = deque([root])
        res = []
        popleft = True
        while myque:
            layer_size = len(myque)
            res.append([])

            if popleft:
                for _ in range(layer_size):
                    node = myque.popleft()
                    res[-1].append(node.val)
                    if node.left:
                        myque.append(node.left)
                    if node.right:
                        myque.append(node.right)
                popleft = False
            else:
                for _ in range(layer_size):
                    node = myque.pop()
                    res[-1].append(node.val)
                    if node.right:
                        myque.appendleft(node.right)
                    if node.left:
                        myque.appendleft(node.left)
                popleft = True
        return res