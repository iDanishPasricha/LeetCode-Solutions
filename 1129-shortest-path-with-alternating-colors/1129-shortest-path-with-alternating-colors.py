class Solution:
    def shortestAlternatingPaths(self, n: int, red_edges: List[List[int]], blue_edges: List[List[int]]) -> List[int]:
        graph = {i: [[], []] for i in range(n)}  # node: [red edges list], [blue edges list]
        for [i, j] in red_edges:
            graph[i][0].append(j)
        for [i, j] in blue_edges:
            graph[i][1].append(j)
   
        ans=[math.inf]*n;
        ans[0]=0;
        visited = set();
        q=deque();
        q.append((0,'r'));
        q.append((0,'b'));
        shortest_distance_from_zero=0;
        while q:
            shortest_distance_from_zero+=1;
            
            for i in range(len(q)):
                node,color=q.popleft();
                if (node,color) not in visited:
                    visited.add((node,color));
                    if color == 'r':
                        for child in graph[node][1]:
                            q.append((child,'b'))
                            ans[child]=min(ans[child],shortest_distance_from_zero)
                    if color == 'b':
                        for child in graph[node][0]:
                            q.append((child,'r'))
                            ans[child]=min(ans[child],shortest_distance_from_zero)
        for i in range(len(ans)):
            if ans[i]==math.inf: ans[i]=-1;
        return ans
                
    '''
Example :-

node : R    B

0    : [1]  []
1    : []   [3]
2    : []   []
3    : [4]  []
4    : []   [5]
5    : []   []

'''











