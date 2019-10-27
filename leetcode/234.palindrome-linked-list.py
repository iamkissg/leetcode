# Definition for singly-linked list.

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:

    def reverse(self, head):
        cur, pre = head, None
        while cur:
            cur.next, pre, cur = pre, cur, cur.next
        return pre

    def isPalindrome(self, head: ListNode) -> bool:
        # 1. 取值(不考虑进阶)
        # 76 ms	27.3 MB	Python3
        # res = []
        # while head:
        #     res.append(head.val)
        #     head = head.next
        # return res == res[::-1]

        # 2. 快慢指针法
        # 88 ms	24.4 MB	Python3
        if not head:
            return True
        slow, fast = head, head

        while fast and fast.next and fast.next.next:
            slow, fast = slow.next, fast.next.next
        odd = not fast.next

        slow.next, left, right = None, head, slow.next
        reversed_left = self.reverse(left)
        if odd: reversed_left = reversed_left.next

        while right:
            if right.val != reversed_left.val:
                return False
            right, reversed_left = right.next, reversed_left.next
        return True


if __name__ == "__main__":
    sol = Solution()
    lnode = ListNode(1)
    lnode.next = ListNode(2)
    lnode.next.next = ListNode(1)
    lnode.next.next.next = ListNode(1)
    print(sol.isPalindrome(lnode))