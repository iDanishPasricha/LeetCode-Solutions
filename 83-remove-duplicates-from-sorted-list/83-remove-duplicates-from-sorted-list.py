# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head : return head
        curr = head.next
        prev = head
   
        while curr:       
            if curr.val==prev.val:    #condition 1
                prev.next =  curr.next
                curr = curr.next
            else:    #condition 2
                curr = curr.next
                prev = prev.next
        return head
    '''
    1->1->2->3->3   # now condition 1
    P  C
    
    1->2->3->3      # now condition 2
    P  C
    
    1->2->3->3      # now condition 2
       P  C
       
    1->2->3->3      # now condition 1
          P  C
    
    1->2->3->null
          P   C
    
    '''
    
                
        