# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """

        while node.next.next!=None:
            node.val=node.next.val
            node=node.next
        if node.next==None:
            node=None
        if node.next.next==None:
            node.val=node.next.val
            node.next=None