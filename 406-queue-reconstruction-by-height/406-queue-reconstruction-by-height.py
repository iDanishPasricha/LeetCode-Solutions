class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        ans=[] 
        people.sort(key=lambda x: (-x[0], x[1]))
    
        #x[0] == height and x[1] == k value (h,k)
    # sort the array in decreasing order of height 
    # within the same height group, you would sort it in increasing order of k
        for i in people:
            
            ans.insert(i[1], i)
        
        return ans
            # Now let's start the greedy here
            # We insert the entry in the output array based on the k value
            # k will act as a position within the array
    
    

    # eg: Input : [[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]
    # after sorting: [[7,0],[7,1],[6,1],[5,0],[5,2],[4,4]]
    
    
    