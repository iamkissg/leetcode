# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0
        phead = ListNode(None)
        cur = phead
        while l1 and l2:
            val = l1.val + l2.val + carry
            carry, val = divmod(val, 10)
            cur.next = ListNode(val)
            cur, l1, l2 = cur.next, l1.next, l2.next

        while l1:
            val = l1.val + carry
            carry, val = divmod(val, 10)
            cur.next = ListNode(val)
            cur, l1 = cur.next, l1.next
        while l2:
            val = l2.val + carry
            carry, val = divmod(val, 10)
            cur.next = ListNode(val)
            cur, l2 = cur.next, l2.next
        
        if carry:
            val = 0 + carry
            carry, val = divmod(val, 10)
            cur.next = ListNode(val)
            cur = cur.next
        
        return phead.next

if __name__ == "__main__":
    sol = Solution()
    # l1 = ListNode(1)
    # l2 = ListNode(9)
    # l2.next = ListNode(9)
    # print(sol.addTwoNumbers(l1, l2))
    l1 = ListNode(5)
    l2 = ListNode(5)
    print(sol.addTwoNumbers(l1, l2))
    exit()