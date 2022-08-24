# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0,head)
        groupPrev = dummy
        
        def getKth(curr,k):
            while curr and k>0:
                curr = curr.next
                k-=1
            return curr
        # kth Node       = last node in our group
        # groupPrev.next = First Node in our group
        while True:
            Kth_Node = getKth(groupPrev,k)
            if not Kth_Node: break #if kth node does not even exist 1->2->3->4->5 and k=2 so for case of 5 kth node does not exist
            groupNext = Kth_Node.next # define groupnext just like groupPrev
            prev,curr = Kth_Node.next , groupPrev.next
            
            while curr!=groupNext:  #simple reverse in a group
                saved = curr.next
                curr.next = prev
                prev,curr = curr,saved
            
            #now just simply update groupPrev from 1st position to last postion 
            saved = groupPrev.next
            groupPrev.next = Kth_Node
            groupPrev = saved
            
        return dummy.next
                
                
            
            
        
        