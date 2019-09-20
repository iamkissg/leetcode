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
    def sortList2(self, head: ListNode) -> ListNode:
        '''
        把值都取出来, 然后排序, 再重新创建链表
        时间复杂度是 O(n)+O(nlog(n))+O(n), 符合要求, 但是
        空间复杂度是 O(n)
        '''
        if not head:
            return None
        if head.next is None:
            return head

        vals = []
        cur = head
        while cur:
            vals.append(cur.val)
            cur = cur.next
        vals = sorted(vals)

        pHead = ListNode(None)
        cur = ListNode(vals[0])
        pHead.next = cur
        for v in vals[1:]:
            cur.next = ListNode(v)
            cur = cur.next

        return pHead.next
    

    def sortList(self, head: ListNode) -> ListNode:
        '''
        归并排序解法, 代码比较丑, 但是思路没问题:
        先用快慢指针找到链表的中点, 断开, 然后分别排序, 再归并
        '''
        if head is None or head.next is None:
            return head

        left_half, fast, slow = head, head, head
        while slow and fast and fast.next:
            fast = fast.next.next
            # 这一步的目的是为了, 在 fast 到达链表后之后, slow 就不要往前走了
            # 想象两个节点的链表 1 -> 2, fast 刚走就到头, slow 不动, 而 slow.next 开始作为第二段链表
            if fast and fast.next:
                slow = slow.next

        right_half, slow.next = slow.next, None
        left_head, right_head = self.sortList(left_half), self.sortList(right_half)

        if left_head.val < right_head.val:
            cur, left_head = left_head, left_head.next
        else:
            cur, right_head = right_head, right_head.next

        pHead = ListNode(None)  # 头指针
        pHead.next = cur
        while left_head or right_head:
            if left_head is None:
                cur.next = right_head
                cur, right_head = cur.next, right_head.next
            elif right_head is None or left_head.val < right_head.val:
                cur.next = left_head
                cur, left_head = cur.next, left_head.next
            else:
                cur.next = right_head
                cur, right_head = cur.next, right_head.next

        return pHead.next
        


if __name__ == "__main__":
    a = ListNode(34)
    a.next = ListNode(2)
    a.next.next = ListNode(-3)
    a.next.next.next = ListNode(0)
    a.next.next.next.next = ListNode(5)

    sol = Solution()
    print(sol.sortList(a))
