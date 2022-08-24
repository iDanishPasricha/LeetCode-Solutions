class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def merge2Lists(l1,l2):
            start = ListNode(0);
            head = start
            while l1 and l2:
                if l1.val<=l2.val:
                    start.next = l1;
                    l1 = l1.next;
                else:
                    start.next = l2;
                    l2 = l2.next;
                start = start.next;
            start.next = l1 or l2;
            
            return head.next
        
        if not lists or len(lists)==0: return None
        
        while len(lists)>1: #until we have just one list
            temp_lists = []
            for i in range(0,len(lists),2): #2 for pairing
                l1 = lists[i]
                l2 = lists[i+1] if (i+1)<len(lists) else None #check if it is not out of bounce
                temp_lists.append(merge2Lists(l1,l2))
            lists = temp_lists
        return lists[0]
        

        '''We can merge two sorted linked list in O(n) time where nn is the total number of nodes in two lists.
           Sum up the merge process and we can get: O(Nlogk)
           Space complexity : O(1)We can merge two sorted linked lists in O(1) space.
        '''
        '''
        or write this 
        
        if len(lists)==0: return 
        if len(lists)==1: return lists[0]
        else: return merge_2_linked_lists(self.mergeKLists(lists[:len(lists)//2]),self.mergeKLists(lists[len(lists)//2:]))
'''