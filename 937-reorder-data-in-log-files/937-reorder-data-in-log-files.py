class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        Letter_log=[]
        Digit_log=[]
        
        for log in logs:
            
            if(log.split()[1]).isdigit():
                Digit_log.append(log)
            else:
                Letter_log.append(log.split())

        Letter_log.sort(key = lambda x:x[0])

        Letter_log.sort(key = lambda x:x[1:])

        
        for i in range(len(Letter_log)):
            Letter_log[i] = (" ".join(Letter_log[i]))
        Letter_log.extend(Digit_log)
        return Letter_log
    
    
    