class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        ans=[];
        d={};
        for i in range(len(nums)):
            d[nums[i]] = i
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in d and d[complement]!=i:
                return [i,d[complement]]
    ''' --^
    To improve our runtime complexity, we need a more efficient way to check if the complement exists in the array. If the complement exists, we need to get its index. and so for this purpose you know A hash table is the best way to maintain a mapping of each element in the array to its index and Since the hash table reduces the lookup time to O(1), the overall time complexity is O(n)

    better optimised
    While we are iterating and inserting elements into the hash table, we also look back to check if current element's complement already exists in the hash table. If it exists, we have found a solution and return the indices immediately.
    
    d  = {}
    for i in range(len(nums)):
        complement = target - nums[i]
        if complement in d:
            return [i,d[complement]]
        d[nums[i]] = i
    same time and space complexity O(n) and O(n)
'''
    
    
            

                
        