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
            if curr.val==prev.val:
                prev.next =  curr.next
                curr = curr.next
            else:
                curr = curr.next
                prev = prev.next
        return head
                
        