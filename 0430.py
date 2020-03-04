"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""
class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        if head == None:
            return
        curr = head
        ischild = 0
        temp = []
        while True:
            if curr.child == None:
                if curr.next == None:
                    if ischild > 0:
                        ischild -= 1
                        t = temp.pop()
                        curr.next = t
                        t.prev = curr
                        curr = curr.next
                    else:
                        break
                else:
                    curr = curr.next
            elif curr.next == None:
                curr.next = curr.child
                curr.child.prev = curr
                curr.child = None
                curr = curr.next
            else:             
                ischild += 1
                temp.append(curr.next)
                curr.next = curr.child
                curr.child.prev = curr
                curr.child = None
                curr = curr.next
        return head