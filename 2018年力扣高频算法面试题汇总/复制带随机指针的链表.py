"""
# Definition for a Node.
"""
class Node:
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return None
        copied_head = Node(head.val, None, None)
        pHead = Node(None, None, None)
        pHead.next = copied_head

        cur = head
        node_map = {cur: copied_head}
        while cur:
            n = cur.next
            r = cur.random
            if n and n not in node_map:
                new_node = Node(n.val, None, None)
                node_map[n] = new_node
            copied_head.next = node_map.get(n, None)
            if r and r not in node_map:
                new_node = Node(r.val, None, None)
                node_map[r] = new_node
            copied_head.random = node_map.get(r, None)
            cur = cur.next
            copied_head = copied_head.next

        return pHead.next

if __name__ == "__main__":
    node_2 = Node(2, None, None)
    node_2.random = node_2
    node_1 = Node(1, node_2, node_2)
    
    sol = Solution()
    print(sol.copyRandomList(node_1))