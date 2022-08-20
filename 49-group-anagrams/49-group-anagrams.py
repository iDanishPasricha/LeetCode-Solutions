class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d={}
        for i in strs:
            sorted_string = "".join(sorted(i))
            if sorted_string not in d:
                d[sorted_string] = [i]
            else:
                d[sorted_string].append(i)
        return d.values()
                    
                    
                
            
            
            
        