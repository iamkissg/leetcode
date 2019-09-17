# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteNode(self, node):
        """
        这个题目讲得不清晰, 没有给定 head, 莫名其妙的, 按照题设, 不是从 linkedlist 中删除 given node 吗
        但是, 它的意思是, 删除传入的 node, 就这样, 删除这个节点
        看到网友给这个方法取名叫替身攻击- -.
        因为只传入了这个节点, 它之前的信息全无, 也就无从修改指向它的指针了
        因此, 只能说让当前节点变成它的后继节点, 实际删掉的是它的第一后继节点
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next