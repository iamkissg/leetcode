# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        results = []
        jinwei = 0
        while l1 or l2:
            l1_val, l2_val = l1.val if l1 else 0, l2.val if l2 else 0
            jinwei, res = divmod(l1_val + l2_val + jinwei, 10)
            res_node = ListNode(res)
            results.append(res_node)
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        if jinwei != 0:
            results.append(ListNode(jinwei))
        for pre, nex in zip(results[:-1], results[1:]):
            pre.next = nex

        return results[0]

if __name__ == "__main__":
    l1 = ListNode(1)
    l1.next = ListNode(8)
    l2 = ListNode(0)
    
    sol = Solution()
    sol.addTwoNumbers(l1, l2)