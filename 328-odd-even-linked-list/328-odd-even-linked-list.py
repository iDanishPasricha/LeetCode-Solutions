# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0);
        r_e = even = ListNode(0);
        r_o = odd = ListNode(0);
        temp = head;
        i=0;
        while temp:
            if  i%2==0:
                even.next = temp;
                even  = even.next;
            else:
                odd.next = temp;
                odd  = odd.next;
            i+=1
            temp = temp.next;
        odd.next=None
        even.next = r_o.next;
        return r_e.next
        
        
            
                