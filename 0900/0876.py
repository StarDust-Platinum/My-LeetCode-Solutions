# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        if head==None:
            return None
        n = 0
        current = head
        while current:
            n += 1
            current = current.next
        n = n//2
        current = head
        for i in range(n):
            current = current.next
        return current

    def middleNode(self, head):
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow