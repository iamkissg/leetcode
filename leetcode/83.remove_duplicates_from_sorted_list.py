# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return None
        if not head.next:
            return head

        head_of_head = ListNode(0)
        pre_node = head
        head_of_head.next = pre_node
        next_node = head.next

        while next_node:
            if next_node.val == pre_node.val:
                pre_node.next = next_node.next
                next_node = next_node.next
            else:
                next_node = next_node.next
                pre_node  = pre_node.next
        return head_of_head.next


if __name__ == "__main__":
    hd = ListNode(1)
    hd.next = ListNode(1)
    hd.next.next = ListNode(2)
    # hd.next = ListNode(2)
    # hd.next.next = ListNode(2)
    # hd.next.next.next = ListNode(2)
    sol = Solution()
    print(sol.deleteDuplicates(hd))