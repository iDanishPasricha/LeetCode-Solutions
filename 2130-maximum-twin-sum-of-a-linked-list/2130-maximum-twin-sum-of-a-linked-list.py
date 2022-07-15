# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        def reverse(head):
            if not head or head.next is None: return head
            
            rest = reverse(head.next)
            start = head;
            head.next.next = start
            start.next=None
            
            return rest
        
        
        temp=temp1=head
        l=[];
        size=0;
        while(temp):
            l.append(temp.val)
            size+=1;
            temp=temp.next;
        print(l)
        head2 = reverse(head)
    
        temp2 = head2
        l2=[];
        while(temp2):
            l2.append(temp2.val)
            temp2=temp2.next
            
        print(l2)
        max_sum = 0;
        for i in range(size//2):
            max_sum = max(max_sum,l[i]+l2[i])
        return max_sum
            
            
        