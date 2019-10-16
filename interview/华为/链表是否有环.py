# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        # 1.
        # fast, slow = head, head
        # while fast and fast.next:
        #     slow = slow.next
        #     fast = fast.next.next
        #     if slow == fast:
        #         return True
        # else:
        #     False

        # 2.
        # 比快慢指针慢
        node_set = set()
        cur = head
        while cur:
            cur = cur.next
            if cur in node_set:
                return True
            node_set.add(cur)
        return False