class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def merge_2_linked_lists(l1,l2):
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
        
        if len(lists)==0: return 
        if len(lists)==1: return lists[0]
        else: return merge_2_linked_lists(self.mergeKLists(lists[:len(lists)//2]),self.mergeKLists(lists[len(lists)//2:]))
