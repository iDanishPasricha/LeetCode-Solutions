# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next: return head
        temp = head
        return_part = temp.next
        saved = temp.next.next
        
        recursive_part = self.swapPairs(saved)
        
        temp.next.next = head
        temp.next = recursive_part
        
        
        return return_part
    