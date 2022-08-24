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
        currToCopy = {None:None} #this will map curr node to its copy
        curr = head     #We will do this question in 2 pass 
        while curr:     # First we will make a copy of each original node and then map original nodes to their copy nodes
            copyNode = Node(curr.val)
            currToCopy[curr] = copyNode
            curr = curr.next
        
        curr = head
        while curr:
            copyNode = currToCopy[curr]
            copyNode.next = currToCopy[curr.next]
            copyNode.random = currToCopy[curr.random]
            
            curr = curr.next
        
        return currToCopy[head]
        