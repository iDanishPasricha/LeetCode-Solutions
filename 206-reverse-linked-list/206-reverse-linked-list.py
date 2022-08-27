# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        while curr:
            saved = curr.next
            curr.next = prev
            prev,curr = curr,saved
        return prev
        
        
        
'''
        if not head or head.next==None: return head
        
        rest = self.reverseList(head.next)
        
        start = head
        head.next.next = start
        start.next = None
        
        return rest

1->2->3->4->5  
suppose after recursion the scenario is

1->(---) where --- is reversed part i.e 5->4->3->2
S->(---)
so we need to do 
head.next.next = start 
and then ending None
'''