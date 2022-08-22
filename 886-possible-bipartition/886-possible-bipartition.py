from collections import defaultdict as dd
class Solution:
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        graph = dd(list)
        for u,v in dislikes:
            graph[u].append(v)
            graph[v].append(u)
        print(graph)
            
            
        def dfs(curr_color,node):
            color_pallete[node]=curr_color
            
            for neigh in graph[node]:
                if color_pallete[neigh]==curr_color:return False
                
                #je ta neighbour da color same hai curr_node de color naal fer tajamma e false
                
                
                if color_pallete[neigh]==0 and not dfs(-curr_color,neigh): return False
            return True
        
        
        #if color_pallete[neigh]==0 means eh neighbour nawa hai fr esto agge dfs call kr -curr_color naal te check kr je kitte agge depth te jaande jaande aah condition aandi k nhi if color_pallete[neigh]==curr_color  je aagi ta false je time tappa leya fer true
                    
                    
        color_pallete = [0] * (N+1)  
        for i in range(1,N+1):
            if color_pallete[i]==0 and not dfs(1,i): return False
        return True
    
    
    #0-> by default
    #1-> change