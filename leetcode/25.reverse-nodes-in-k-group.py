# Definition for singly-linked list.
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

    def reverse1Group(self, head):
        prev, cur = None, head
        
        while cur:
            cur.next, prev, cur = prev, cur, cur.next
        return prev


    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        
        # 创建一个头指针, 防止头丢了
        pHead = ListNode(0)
        pHead.next = head

        # 用 start, end 去找 k 个节点的子链表
        # start 作为子链表的头指针
        # end 则直到子链表的最后一个节点, 反转过后将作为子链表的头
        start = pHead
        end = head
        while end:
            ch = start.next  # 抽象一个当前子链表的头节点
            for i in range(k-1):
                if end:
                    end = end.next
                else:
                    break
            else:
                if end is not None:
                    # rest 用于保存后续的链表 (如果还有)
                    # 将子链从尾节点处截断, 然后反转
                    rest = end.next
                    end.next = None
                    end = self.reverse1Group(ch)

                    # 交换之前, 明确:
                    # ch 现在是当前子链的尾节点, 其后接暂存的链表
                    # end 是反转子链的头, 所以更新头指针从 ch 指向 end
                    # 更新下一段子链, 所以移动头指针
                    # 子链内的指针不用管, 已经在 reverse1Group 中被反转了
                    start.next, start, ch.next = end, ch, rest
                    end = rest

        return pHead.next

if __name__ == "__main__":

    sol = Solution()
    a = ListNode(1)
    a.next = ListNode(2)
    a.next.next = ListNode(3)
    a.next.next.next = ListNode(4)
    a.next.next.next.next = ListNode(5)
    print(1, sol.reverseKGroup(a, 1))
    a = ListNode(1)
    a.next = ListNode(2)
    a.next.next = ListNode(3)
    a.next.next.next = ListNode(4)
    a.next.next.next.next = ListNode(5)
    print(2, sol.reverseKGroup(a, 2))
    a = ListNode(1)
    a.next = ListNode(2)
    a.next.next = ListNode(3)
    a.next.next.next = ListNode(4)
    a.next.next.next.next = ListNode(5)
    print(3, sol.reverseKGroup(a, 3))
    a = ListNode(1)
    a.next = ListNode(2)
    a.next.next = ListNode(3)
    a.next.next.next = ListNode(4)
    a.next.next.next.next = ListNode(5)
    print(4, sol.reverseKGroup(a, 4))
    a = ListNode(1)
    a.next = ListNode(2)
    a.next.next = ListNode(3)
    a.next.next.next = ListNode(4)
    a.next.next.next.next = ListNode(5)
    print(5, sol.reverseKGroup(a, 5))
    