# Definition for singly-linked list.
from Queue import PriorityQueue


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists):

        head = point = ListNode(0)
        pq = PriorityQueue()
        for l_node in lists:
            if l_node:
                pq.put((l_node.val, l_node))
        while not pq.empty():
            val, node = pq.get()
            point.next = ListNode(val)
            node = node.next
            point = point.next
            if node:
                pq.put((node.val, node))
        return head.next
