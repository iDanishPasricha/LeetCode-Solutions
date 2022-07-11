# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        c1=c2=0;
        temp1=headA;
        temp2=headB;
        
        while(temp1):
            c1+=1;
            temp1=temp1.next;
        while(temp2):
            c2+=1;
            temp2=temp2.next;
        diff = abs(c1-c2)
        curr1=headA;
        curr2=headB;
        
        if c1>c2:
            for i in range(diff):
                curr1=curr1.next;
        else:
            for i in range(diff):
                curr2=curr2.next;
        while(curr1!=curr2):
            curr1=curr1.next;
            curr2=curr2.next;
        return curr1
            
            
            
            
        