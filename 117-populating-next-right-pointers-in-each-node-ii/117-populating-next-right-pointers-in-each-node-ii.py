"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root: return root
        else:
            q=[];
            q.append(root)
            tail = root
            while(q):
                curr = q.pop(0);
                if curr.left:
                    q.append(curr.left);
                if curr.right:
                    q.append(curr.right);
                
                if curr == tail:
                    curr.next=None
                    if len(q)>0:
                        tail = q[-1];
                    else:
                        tail = None
                else:
                    curr.next = q[0]
            return root
                