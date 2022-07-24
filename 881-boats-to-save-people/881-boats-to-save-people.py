class Solution:
    def numRescueBoats(self, people, limit):
        people = sorted(people)[::-1]
        i = 0;
        j = len(people)-1
        while(i<=j):
            if people[i]+people[j]<=limit:
                i+=1;
                j-=1;
            else:
                i+=1;
        return i
            
        '''
Sort people.

For the current heaviest person, we try to let him go with the lightest person.
As all people need to get on the boat.
If the sum of weight is over the limit, we have to let the heaviest go alone.
No one can take the same boat with him.

At the end of for loop, it may happend that i = j.
But it won't change the result so don't worry about it.

Time Complexity:
O(NlogN)
'''