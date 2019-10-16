# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # def reverseList(self, head: ListNode) -> ListNode:
    #     cur, pre = head, None
    #     while cur:
    #         cur, pre, pre.next = cur.next, cur, pre
    #     return pre

    def reverseList(self, head: ListNode) -> ListNode:
        new_head, new_tail = self.reverseList_recursively(head)
        return new_head
    
    def reverseList_recursively(self, head: ListNode) -> ListNode:
        if not head:
            return None
        if not head.next:
            return head, head
        
        cur, nxt = head, head.next
        new_head, new_tail = self.reverseList_recursively(nxt)
        cur.next = None
        new_tail.next = cur
        return new_head, cur