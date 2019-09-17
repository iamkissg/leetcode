# Definition for singly-linked list.
from copy import copy


class ListNode(object):
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


class Solution(object):
    def isPalindrome(self, head):
        """
        取值法, 如果不定义 ListNode 的等价标准, listnode_a == listnode_b 不能确定
        :type head: ListNode
        :rtype: bool
        """
        node_vals = []
        cur = head
        while cur:
            node_vals.append(cur.val)
            cur = cur.next
        return node_vals == node_vals[::-1]

    def reverseLinkedList(self, head):
        cur, prev = head, None
        while cur:
            cur.next, prev, cur = prev, cur, cur.next
        return prev

    def isPalindrome2(self, head):
        """
        快慢指针+反转链表法
        :type head: ListNode
        :rtype: bool
        """
        fast, slow, slow2 = head, head, head
        while slow and fast and fast.next:
            slow, fast = slow.next, fast.next.next

        slow = self.reverseLinkedList(slow)
        while slow:
            if slow.val != slow2.val:
                return False
            slow, slow2 = slow.next, slow2.next
        return True
        

if __name__ == "__main__":
    a = ListNode(1)
    a.next = ListNode(2)
    a.next.next = ListNode(1)

    sol = Solution()
    print(sol.isPalindrome2(a))