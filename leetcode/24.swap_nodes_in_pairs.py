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
    def swapPairs(self, head: ListNode) -> ListNode:
        '''题解来自覃超的算法课'''

        # prev 赋一个 self, 不明觉厉, 似乎是起到哑节点的作用
        # 现在, prev.next 指向传入的链表表头
        # prev 会跟着向前传播
        # prev, prev.next = self, head

        # 根据网友的解答, 下面的做法也完全没有问题
        # 不知道为啥头指针保存住了
        pHead = ListNode(0)
        prev, prev.next = pHead, head

        while prev.next and prev.next.next:
            a = prev.next
            b = a.next
            # 节点的两两交换
            # 指向前一个节点的指针, 现在要指向后一个节点, 即交换后的前一个节点
            # 后一个节点的指针指向前一个节点, 前一个节点的指针指向后一个节点的后一个节点, 完成交换
            prev.next, b.next, a.next = b, a, b.next
            prev = a

        return pHead.next


if __name__ == "__main__":
    sol = Solution()
    a = ListNode(1)
    a.next = ListNode(2)
    a.next.next = ListNode(3)
    a.next.next.next = ListNode(4)
    a.next.next.next.next = ListNode(5)
    print(sol.swapPairs(a))