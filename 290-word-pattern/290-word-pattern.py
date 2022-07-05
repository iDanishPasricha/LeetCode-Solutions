class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        li = s.split(' ')
        print(li)
        d = {}
        if len(li) != len(pattern): return False
        
        for i, val in enumerate(pattern):
            print(i,val)
            if val in d and d[val] != li[i]: return False
            elif val not in d and li[i] in d.values(): return False
            elif val not in d:
                d[val] = li[i]
                print(d)
                    
        return True
        