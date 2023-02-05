# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def rec(p,c):
            if not c:
                return p
            t = rec(c,c.next)
            c.next = p
            return t
        
        return rec(None,head) 

        
        