# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        '''
        20191005
        执行用时 :40 ms, 在所有 Python3 提交中击败了96.57% 的用户
        内存消耗 :13.8 MB, 在所有 Python3 提交中击败了5.53%的用户
        '''
        phead=  ListNode(None)
        phead.next = head
        slow, fast = phead, head
        for _ in range(n):
            fast = fast.next

        while fast:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next

        return phead.next
