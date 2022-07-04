class Solution:
    def findClosestElements(self, nums: List[int], k: int, x: int) -> List[int]:
        def binary_search(nums,start,end,x):
            while(start<=end):
                mid=(start+end)//2;
                if x==nums[mid]:return mid
                if x>nums[mid]: start=mid+1;
                else:end=mid-1;
            return start
        
        def kclosest(left,right,limit):
            while (limit!=0):
                if limit==0:return ans
                if left==-1: #je left aale cover kr laye saare fer right aale paase aaja 
                    ans.append(nums[right])
                    right+=1;
                elif right==len(nums): #je right aale cover kr laye saare fer left aale paase aaja 
                    ans.insert(0,nums[left])
                    left-=1;
                elif abs(nums[left]-x)<=abs(nums[right]-x): #pehli preference left side waale number nu 
                    ans.insert(0,nums[left])
                    left-=1;
                else: #hun je left side ala distance vadda e fer right aala paa de
                    ans.append(nums[right])
                    right+=1;
                
                limit-=1;
            return ans
        if x<=nums[0]: return nums[:k]
        elif x>=nums[-1]: return nums[-k:]
        elif nums[0]<x<nums[-1]:
            ans=[];
            index=binary_search(nums,0,len(nums)-1,x)
            return kclosest(index-1,index,k)
        