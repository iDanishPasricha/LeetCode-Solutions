# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head):
        dummy = new = ListNode(0,head)
        
        while head and head.next:
            if head.val==head.next.val:
                while  head and head.next and head.val== head.next.val:
                    head = head.next
                head = head.next
                new.next = head
            else:
                new = new.next
                head = head.next
        return dummy.next
                
              
        

    


            
        

            
        
        