# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        dummy = ListNode(0)
        dummy.next = head
        grpprev = dummy

        while True:
            
            kth = grpprev
            for _ in range(k):
                kth = kth.next
                if not kth:
                    return dummy.next
                
            grpnext = kth.next

            prev = grpnext
            curr = grpprev.next

            while curr != grpnext:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
            
            nxt = grpprev.next
            grpprev.next = kth
            grpprev = nxt
            
