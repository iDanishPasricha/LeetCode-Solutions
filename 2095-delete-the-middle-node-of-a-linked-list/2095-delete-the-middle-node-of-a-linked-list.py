# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: return head
        if head.next is None: return 
        size=0;
        temp=curr=head;
        while(temp):
            size+=1;
            temp = temp.next
        mid = size//2;
        for i in range(mid-1):
            curr=curr.next
        saved = curr.next.next
        curr.next = saved
        return head
            
        