class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        symbols = "!?',;.";
        
        for s in symbols:
            paragraph = paragraph.replace(s," ")
        print(paragraph)
    
        paragraph = paragraph.lower()
        paraList = paragraph.split()
        
        
        
        
        d = {}
        for w in paraList:
            if w not in banned:
                if w not in d.keys():
                    d[w] = 1 
                else:
                    d[w] += 1
        
        maxVal = max(d.values())
        for k,v in d.items():
            if v == maxVal: return k
        