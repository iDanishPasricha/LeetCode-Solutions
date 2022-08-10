import heapq

class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        
        # Organize the heap based on the "ratio improvement factor"
        # i.e. The (new ratio) - (old ratio), the one that will improve the largest should be the one added to
        # Add a negative since all heaps are minimum-oriented in python
        classes = [[-((p+1)/(t+1) - (p/t)), p, t] for p, t in classes]
        heapq.heapify(classes)
        
        # Go through the amount of students we need to add
        for _ in range(extraStudents):
            # Remove the next largest opportunity
            c = heapq.heappop(classes)
            
            # Change all of the values
            c[1] += 1
            c[2] += 1
            # Update ratio factor
            c[0] = -((c[1]+1)/(c[2]+1) - (c[1]/c[2]))
            # Push this back on to the heap
            heapq.heappush(classes, c)
            
        # Calculate the total pass ratio after doing this
        total_ratio = 0
        n = 0
        for c in sorted(classes):
            n += 1
            total_ratio += (c[1] / c[2])
            
        return total_ratio / n