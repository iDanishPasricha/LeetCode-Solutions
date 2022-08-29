class Solution:
    def combinationSum4(self, nums: List[int], amount: int) -> int:
        def get_ways(amount,coins,d):
            
            if amount<0: return 0
            if amount==0: return 1
            if amount in d.keys(): return d[amount]
            
            else:
                total_ways=0
                for i in range(len(coins)):
                    coin=coins[i];
                    if coin > amount: continue
                    else:
                        one_way = get_ways(amount-coin, coins , d)
                        if one_way>0: total_ways+=one_way
                            
                d[amount] = total_ways
                print(d)
                return total_ways
            
            
        
        d={};
        return get_ways(amount,nums,d);