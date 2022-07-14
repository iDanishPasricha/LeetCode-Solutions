# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, nums: List[List[int]]) -> Optional[TreeNode]:
        d={};
        l=[];
        for i in nums:
            for j in range(len(i[:-1])):l.append(i[j])
            d[i[1]]=True
        final_l = list(set(l));
        for i in final_l:
            if i not in d.keys():
                root_val = i;
        print(root_val)
        
        
        
        
        
        
        
        
        graph={};
        for i in nums:
            if i[0] in graph:
                if i[2]==1: graph[i[0]][0] = i[1]
                if i[2]==0: graph[i[0]][1] = i[1]
                
            else:
                graph[i[0]] = [None,None]

                if i[2]==1:
                    graph[i[0]][0] = i[1]
                if i[2]==0:
                    graph[i[0]][1] = i[1]
        

                
                
                
                
                
                
                
        print(graph)
        def dfs(node):
            
            if not node: return 
            if node not in graph: return TreeNode(node)
            
            temp = TreeNode(node)
            if graph[node][0]:
                temp.left = dfs(graph[node][0])
            if graph[node][1]:
                temp.right = dfs(graph[node][1])
            return temp
            
                
                
    
        return dfs(root_val)

        