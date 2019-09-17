# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        使用 set 保存走过路径的笨办法, 不满足`程序尽量满足 O(n) 时间复杂度，且仅用 O(1) 内存`要求
        O(n+m) 时间复杂度, O(n) 内存h
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if not headA or not headB:
            return None

        cur = headA
        passed_nodes = {cur}
        while cur:
            passed_nodes.add(cur)
            cur = cur.next
        cur = headB
        while cur:
            if cur in passed_nodes:
                return cur
            cur = cur.next
        else:
            return None

    def getIntersectionNode(self, headA, headB):
        '''
        神奇的解法, 代码还漂亮
        '''
        pA = headA
        pB = headB
        while pA != pB:
            pA = pA.next if pA else headB
            pB = pB.next if pB else headA
        return pA

        
if __name__ == "__main__":
    node = ListNode(8)
    node.next = ListNode(4)
    node.next.next = ListNode(5)
    node1 = ListNode(4)
    node1.next = ListNode(1)
    node1.next.next = node
    node2 = ListNode(5)
    node2.next = ListNode(0)
    node2.next.next = ListNode(1)
    node2.next.next.next = node

    sol = Solution()
    print(sol.getIntersectionNode(node1, node2).val)

