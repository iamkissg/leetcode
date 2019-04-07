# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    
    # Time Limit Exceeded
    # def isSymmetric(self, root: TreeNode) -> bool:
    #     from queue import Queue

    #     def is_symmetric(que):
    #         return que == que[::-1]

    #     if not root:
    #         return True
    #     if root and not root.left and not root.right:
    #         return True

    #     Q = Queue()
    #     Q.put(root)
    #     count = 1
    #     while Q.qsize():
    #         l = []
    #         for i in range(count):
    #             node = Q.get_nowait()
    #             if node:
    #                 l.append(node.val)
    #                 Q.put(node.left)
    #                 Q.put(node.right)
    #             else:
    #                 l.append(None)
    #                 Q.put(None)
    #                 Q.put(None)

    #         if not is_symmetric(l):
    #             return False
    #         if all([e is None for e in l]):
    #             break
    #         count *= 2
    #     return True

    def isSymmetric(self, root: TreeNode) -> bool:
        from queue import deque

        if not root:
            return True
        if root and not root.left and not root.right:
            return True

        Q = deque()
        Q.append(root.left)
        Q.append(root.right)
        while len(Q):
            left = Q.popleft()
            right = Q.popleft()
            if (left and not right) or (right and not left):
                return False
            elif not (left or right):
                continue
            elif left.val != right.val:
                return False

            Q.append(left.left)
            Q.append(right.right)
            Q.append(left.right)
            Q.append(right.left)
        else:
            return True


if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(2)
    # root.left.left = None
    # root.left.right = TreeNode(3)
    # root.right.left = TreeNode(3)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(4)
    root.right.left = TreeNode(4)
    root.right.right = TreeNode(3)

    sol = Solution()
    print(sol.isSymmetric(root))