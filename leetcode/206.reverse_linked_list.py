# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        return super().__str__()

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        cur, prev = head, None

        while cur:
            # 神奇的连等式, 先执行等号右边, 把值都准备好了, 然后左边分别赋值
            cur.next, prev, cur = prev, cur, cur.next
        return cur


if __name__ == "__main__":
    sol = Solution()
    a = ListNode(1)
    a.next = ListNode(2)
    a.next.next = ListNode(3)
    a.next.next.next = ListNode(4)
    a.next.next.next.next = ListNode(5)
    print(sol.reverseList(a))