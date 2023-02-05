# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        a = b = head
        count = 0
        while a:
            count+=1
            a = a.next
        mid = count // 2
        po = 0
        while b:
            if po == mid:
                return b
            else:
                b = b.next
                po+=1
        return None
            
            

        