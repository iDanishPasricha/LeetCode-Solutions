class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        rooms_visited=[False]*len(rooms); 
        rooms_visited[0]=1;
        q = deque([0])
        while q:
            curr=q.popleft();
            for i in rooms[curr]:
                if rooms_visited[i]==False:
                    rooms_visited[i]=True;
                    q.append(i);
        return all(rooms_visited)
    
    
        ans=[];
        def dfs(curr,temp):
            if curr == len(graph)-1:
                ans.append(temp.copy())
                return
            for neighbor in graph[curr]:
                temp.append(neighbor)
                dfs(neighbor,temp)
                temp.pop()
                

        dfs(0,[0]);
        return ans
        
        
        
        