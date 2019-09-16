# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    # def hasCycle(self, head):
    #     """
    #     :type head: ListNode
    #     :rtype: bool
    #     """
    #     passed_nodes = set()

    #     cur = head
    #     while cur:
    #         if cur in passed_nodes:
    #             return True
    #         passed_nodes.add(cur)
    #         cur = cur.next
    #     else:
    #         return False

    def hasCycle(self, head):
        """
        快慢指针法
        :type head: ListNode
        :rtype: bool
        """
        fast = slow = head

        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        else:
            return False



if __name__ == "__main__":
    sol = Solution()
    a = ListNode(1)
    a.next = ListNode(2)
    a.next.next = ListNode(3)
    a.next.next.next = ListNode(4)
    a.next.next.next.next = ListNode(5)
    print(sol.hasCycle(a))
    a.next.next.next.next.next = a
    print(sol.hasCycle(a))