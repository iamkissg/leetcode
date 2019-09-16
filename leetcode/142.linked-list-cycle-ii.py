# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def detectCycle2(self, head):
        """
        集合法, 需要额外的存储空间
        :type head: ListNode
        :rtype: ListNode
        """
        cur = head
        idx = 0
        passed_dict = {}
        while cur:
            if cur in passed_dict:
                # return passed_dict[cur]  # 返回从表头开始的索引位置, 本题要求返回节点
                return cur
            passed_dict[cur] = idx
            cur = cur.next
            idx += 1
        else:
            return None

    
    # def detectCycle(self, head):
    #     """
    #     在有环的情况下, 第一次检测到环不存在了, 说明已经是环的第二个节点了, 此时不需要额外的存储空间, 但是要多次检测
    #     这个时候要断开链, 要千万小心, 要复原, 不然还是错的, 但是破镜似难圆啊
    #     :type head: ListNode
    #     :rtype: ListNode
    #     """
    #     pass


    def detectCycle(self, head):
        """
        快慢指针法
        :type head: ListNode
        :rtype: bool
        """
        fast = slow = head

        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            # 检测到环, 第二阶段, 找到环入口
            # https://leetcode-cn.com/problems/linked-list-cycle-ii/solution/huan-xing-lian-biao-ii-by-leetcode/
            # 快慢指针解法, 当两个指针的相遇点, 距离环入口的距离恰好等于链表头到环入口的距离
            if slow == fast:
                p1 = head
                p2 = slow
                while p1 != p2:
                    p1 = p1.next
                    p2 = p2.next
                return p1
        else:
            return None

        
if __name__ == "__main__":
    sol = Solution()
    a = ListNode(1)
    a.next = ListNode(2)
    a.next.next = ListNode(3)
    a.next.next.next = ListNode(4)
    a.next.next.next.next = ListNode(5)
    print(sol.detectCycle(a))
    a.next.next.next.next.next = a.next
    print(sol.detectCycle2(a))
    print(sol.detectCycle(a))