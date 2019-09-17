# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        cur = self
        vals = []
        while cur:
            vals.append(cur.val)
            cur = cur.next
        return ''.join(map(str, vals))

class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head:
            return None
        if head.next is None:
            return head

        p_A, p_B1, p_B2 = head, head.next, head.next

        while p_A and p_B1 and p_A.next and p_B1.next:
            p_A.next = p_A.next.next
            p_A = p_A.next
            p_B1.next = p_B1.next.next
            p_B1 = p_B1.next
        p_A.next = p_B2

        return head

if __name__ == "__main__":

    a = ListNode(1)
    a.next = ListNode(2)
    a.next.next = ListNode(3)
    a.next.next.next = ListNode(4)
    a.next.next.next.next = ListNode(5)

    sol = Solution()
    print(sol.oddEvenList(a))