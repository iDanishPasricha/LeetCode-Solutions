class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        visited=set();
        def dfs(index):
            if index>=len(arr) or index<0: return False
            if index in temp: return True 
            if index not in visited:
                visited.add(index);
                return dfs(index+arr[index]) or dfs(index-arr[index]);
        
        temp=[];
        for i in range(len(arr)):
            if arr[i]==0:
                temp.append(i);
        print(temp)
        return dfs(start)