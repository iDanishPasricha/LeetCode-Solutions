class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        
        if end not in bank:return -1
        
        #check each position and insert ['A','C','G','T'] and check
        # if this new mutation is in bank steps+1 else continue
        visited=set();
        q=deque();
        q=[start]
        visited.update(q);
        bank.append(start);
        choice=['A','C','G','T'];
        steps=0;
        
        while q:
            for i in range(len(q)):
                curr_mut = q.pop(0);
                if curr_mut == end: return steps;
                if curr_mut not in bank:continue
                for i in range(len(start)):
                    for j in range(len(choice)):
                        new_mut = curr_mut[:i]+choice[j]+curr_mut[i+1:]
                        if new_mut not in visited:
                            visited.add(new_mut);
                            q.append(new_mut);
            steps+=1;
        return -1
                    