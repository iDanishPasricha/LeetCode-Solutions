class Solution:
    def groupAnagrams(self,strs):
        d = {}
        
        for s in strs:
            character_array = [0] * 26 #character count 
            
            for char in s:
                character_array[ord(char) - ord('a')] += 1
            if tuple(character_array) not in d:
                d[tuple(character_array)] = [s]
            else:
                d[tuple(character_array)].append(s)
        return d.values()
        
'''
Two strings are anagrams if and only if their character counts (respective number of occurrences of each character) are the same.

lets say {
          (2,1,0,0,.....,0):["aab","aba","baa"],
          (1,2,3,0,.....,0): ["abbccc"]
          }
Time Complexity: O(NK), where N is the length of strs, and K is the maximum length of a string in strs. Counting each string is linear in the size of the string, and we count every string.

Space Complexity: O(NK), the total information content stored in ans.

Another approach basic 
        d={}
        for i in strs:
            sorted_string = "".join(sorted(i))
            if sorted_string not in d:
                d[sorted_string] = [i]
            else:
                d[sorted_string].append(i)
        return d.values()
                    
        
Time Complexity: O(NKlogK), where N is the length of strs, and K is the maximum length of a string in strs. The outer loop has complexity O(N) as we iterate through each string. Then, we sort each string in O(KlogK) time.

Space Complexity: O(NK), the total information content stored in ans.
'''
                    
                
            
            
            
        