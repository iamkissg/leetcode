# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:

        if not (l1 or l2):
            return None

        if l1 and not l2:
            return l1
        
        if l2 and not l1:
            return l2

        if l1.val <= l2.val:
            res = l1
            l1 = l1.next
        else:
            res = l2
            l2 = l2.next
        
        current = res

        while l1 or l2:
            if l1 and not l2:
                current.next = l1
                current = current.next
                l1 = l1.next
                continue
            if l2 and not l1:
                current.next = l2
                current = current.next
                l2 = l2.next
                continue

            l1_val = l1.val
            l2_val = l2.val

            if l1_val <= l2_val:
                current.next = l1
                current = current.next
                l1 = l1.next
            else:
                current.next = l2
                current = current.next
                l2 = l2.next

        return res

if __name__ == "__main__":
    pass
            