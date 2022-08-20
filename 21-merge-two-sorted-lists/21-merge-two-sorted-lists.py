# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        head = ListNode(0);
        reserve = start = head
        while l1 and l2:
            if l1.val<=l2.val:
                start.next=l1;
                l1=l1.next;
            else:
                start.next=l2;
                l2=l2.next;
            start=start.next;
        start.next = l1 or l2;
        return reserve.next
    
'''
    Time complexity : O(n + m)O(n+m)

Because exactly one of l1 and l2 is incremented on each loop iteration, the while loop runs for a number of iterations equal to the sum of the lengths of the two lists. All other work is constant, so the overall complexity is linear.

Space complexity : O(1)O(1)

The iterative approach only allocates a few pointers, so it has a constant overall memory footprint.
'''
    
    