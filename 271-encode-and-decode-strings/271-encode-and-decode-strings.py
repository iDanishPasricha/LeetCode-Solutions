class Codec:
    def encode(self, strs):
        ans = ""
        for i in strs:
            ans+=str(len(i))+"#"+i
        return ans
        

    
    def decode(self, s):
        ans = []
        i = 0
        
        while i<len(s):
            j = i
            while(s[j]!="#"):
                j+=1;
            length = int(s[i:j])
            ans.append(s[j+1:j+1+length])
            i = j+1+length
        return ans