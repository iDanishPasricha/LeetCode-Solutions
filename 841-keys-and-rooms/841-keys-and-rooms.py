class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        rooms_visited=[False]*len(rooms); 
        rooms_visited[0]=True;
        q = deque([0])
        while q:
            curr=q.popleft();
            for i in rooms[curr]:
                if rooms_visited[i]==False:
                    rooms_visited[i]=True;
                    q.append(i);
        return all(rooms_visited)
    
        
        
        