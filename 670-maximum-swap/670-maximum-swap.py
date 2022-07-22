class Solution:
    def maximumSwap(self, num: int) -> int:
        def check_possible_candidates(current_index,number,array,integers):
            possible_candidates = integers[number+1:][::-1]
            for i in possible_candidates:
                if last_index_array[i]<=current_index: continue
                else:
                    return last_index_array[i]
                    break
            return -1
        
        integers = [0,1,2,3,4,5,6,7,8,9]
        last_index_array = {i:0 for i in range(10)};
        nums = [int(x) for x in str(num)]
        for i in range(len(nums)):
            last_index_array[nums[i]]=i;
        for i in range(len(nums)):
            temp = check_possible_candidates(i,nums[i],nums[i+1:],integers);
            if temp!=-1:
                nums[i],nums[temp] = nums[temp],nums[i]
                break
        s = [str(i) for i in nums]
        ans = int("".join(s))
        return ans
        
                
            
        