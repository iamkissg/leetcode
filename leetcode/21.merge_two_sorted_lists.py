# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:

        if not (l1 or l2):
            return None

        if l1 and not l2:
            return l1
        
        if l2 and not l1:
            return l2

        if l1.val <= l2.val:
            res = l1
            l1 = l1.next
        else:
            res = l2
            l2 = l2.next
        
        current = res

        while l1 or l2:
            if l1 and not l2:
                current.next = l1
                current = current.next
                l1 = l1.next
                continue
            if l2 and not l1:
                current.next = l2
                current = current.next
                l2 = l2.next
                continue

            l1_val = l1.val
            l2_val = l2.val

            if l1_val <= l2_val:
                current.next = l1
                current = current.next
                l1 = l1.next
            else:
                current.next = l2
                current = current.next
                l2 = l2.next

        return res

    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        '''20190920'''
        # 一个链表为空的情况下, 返回另一条链表
        if not l1:
            return l2
        if not l2:
            return l1

        ha, hb = l1, l2
        phc = ListNode(None)  # 作合合并后链表的 head 的头指针
        if ha.val < hb.val:
            hc, ha = ha, ha.next
        else:
            hc, hb = hb, hb.next
        phc.next = hc

        while ha or hb:
            if not ha:
                hc.next, hb = hb, hb.next
            elif not hb:
                hc.next, ha = ha, ha.next
            elif ha.val < hb.val:
                hc.next, ha = ha, ha.next
            else:
                hc.next, hb = hb, hb.next
            hc = hc.next    

        return phc.next

if __name__ == "__main__":
    pass
            