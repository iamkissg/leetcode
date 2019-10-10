# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:

    def reverseBetween_recursively(self, head, m, n):
        """
        20191011
        
        Leetcode 官方提供的递归解法, 基于类似数组的交换双指针指节点值的做法
        """

        if not head:
            return None

        left, right = head, head
        stop = False
        def recurseAndReverse(right, m, n):
            # 这里取巧了, nonlocal 可以取得域外但是非全局的变量
            # nonlocal keyword that allows you to assign to variables in an outer, but non-global, scope
            nonlocal left, stop

            # 递归终止条件
            # base case. Don't proceed any further
            if n == 1:
                return

            # 在到达递归终止条件之前 (即到达交换链表的右边界), 右指针一直项右滑动
            # Keep moving the right pointer one step forward until (n == 1)
            right = right.next

            # 左指针的情况和右指针一样, 在到达交换链表的左边界后就停止移动
            if m > 1:
                left = left.next

            # 在递归返回之前, 后面的函数不会执行, 于是右指针一直走到交换链表的右边界, 而左指针在更早的时候就停在了左边界
            # 然后开始走下面的步骤, 交换值, 并递归返回
            recurseAndReverse(right, m - 1, n - 1)

            # 这是交换的终止条件, 交换左右指针的值之后, 左右指针相向而行, 直到两者相遇, 或右指针到了左指针左边
            if left == right or right.next == left:
                stop = True

            # Until the boolean stop is false, swap data between the two pointers     
            if not stop:
                left.val, right.val = right.val, left.val

                # 交换一次之后, 左指针右移一步, 然后函数返回, 相当于右指针回退了一步
                # 左指针通过 nonlocal 一直跟着跑
                left = left.next           

        recurseAndReverse(right, m, n)
        return head


    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if m == n:
            return head

        phead = ListNode(None)
        phead.next = head

        cur, pre = head, None
        i = 1
        while cur:
            if i == m:
                r_end = cur
            if i == n:
                r_start = cur

            if m < i < n:
                cur.next, cur, pre = pre, cur.next, cur
            else:
                cur, pre = cur.next, cur
            i += 1

        return phead

if __name__ == "__main__":
    ll = ListNode(1)
    ll.next = ListNode(2)
    ll.next.next = ListNode(3)
    ll.next.next.next = ListNode(4)
    ll.next.next.next.next = ListNode(5)

    sol = Solution()
    print(sol.reverseBetween(ll, 2, 4))