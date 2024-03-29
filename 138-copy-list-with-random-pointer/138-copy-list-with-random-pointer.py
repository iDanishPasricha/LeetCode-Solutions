"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        currToCopy = {None:None} #this will map curr node to its copyNode
        curr = head     #We will do this question in 2 pass 
        while curr:     # First we will make a copy of each original node and then map original nodes to their copy nodes
            copyNode = Node(curr.val)
            currToCopy[curr] = copyNode
            curr = curr.next
        
        curr = head
        while curr:  #in the second pass we will assign next and randon to these copy nodes
            copyNode = currToCopy[curr]
            copyNode.next = currToCopy[curr.next] #whatever will be original node's next will also be copy nodes' next
            copyNode.random = currToCopy[curr.random]
            
            curr = curr.next
        
        return currToCopy[head]
    
    #O(n)
    #O(n)
        