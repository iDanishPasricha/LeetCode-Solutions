class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:

        def sorting(log):
            arr = log
            n = len(log)
            # basically bubble sort
            for i in range(n): 
            # Last i elements are already in place 
                for j in range(0, n-i-1): 
                    if arr[j][1:] > arr[j+1][1:]:  #The letter-logs are sorted lexicographically by their contents.
                        arr[j], arr[j+1] = arr[j+1], arr[j]
                    elif (arr[j][1:] == arr[j+1][1:]): 
                        #If their contents are the same, then sort them lexicographically by their identifiers.
                        if arr[j][0] > arr[j+1][0]:
                            arr[j], arr[j+1] = arr[j+1], arr[j]
            return arr
        
        
        Letter_log=[]
        Digit_log=[]
        
        for i in logs:
            new_i = i.split()
            if(new_i[1]).isdigit():
                Digit_log.append(i)
            else:
                Letter_log.append(new_i)
                
        Letter_log = sorting(Letter_log)
        
        for i in range(len(Letter_log)):
            Letter_log[i] = (" ".join(Letter_log[i]))
        Letter_log.extend(Digit_log) #The letter-logs come before all digit-logs.
        return Letter_log
    
    
    '''
    another way
    instead of sorting function just these 2 :
    
        Letter_log.sort(key = lambda x:x[0])
        Letter_log.sort(key = lambda x:x[1:])
    
    '''
    