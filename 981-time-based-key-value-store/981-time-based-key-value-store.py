'''
 it is mentioned that "All the timestamps of set are strictly increasing", thus even if we use an array to store the timestamps, they will be pushed in sorted order. But we also need to store values with each timestamp, so we will store (timestamp, value) pairs in the key's bucket which will be an array.




Algorithm
Create a hashmap keyTimeMap which stores string as key and an array of pairs as value, as discussed.

In the set() function, push (timestamp, value) pair in bucket key in keyTimeMap.

In the get() function, we find time equal to or less than timestamp using binary-search on the array.

If no time equal to or less than timestamp exists, we return an empty string.
Otherwise, we return the value stored at the time equal to or just less than timestamp.
'''
class TimeMap:
    def __init__(self):
        self.key_time_map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        # If the 'key' does not exist in dictionary.
        if not key in self.key_time_map:
            self.key_time_map[key] = []
            
        # Store '(timestamp, value)' pair in 'key' bucket.
        self.key_time_map[key].append([ timestamp, value ])
        

    def get(self, key: str, timestamp: int) -> str:
        # If the 'key' does not exist in dictionary we will return empty string.
        if not key in self.key_time_map:
            return ""
        
        if timestamp < self.key_time_map[key][0][0]:
            return ""
        
        left = 0
        right = len(self.key_time_map[key])
        
        while left < right:
            mid = (left + right) // 2
            if self.key_time_map[key][mid][0] <= timestamp:
                left = mid + 1
            else:
                right = mid

        # If iterator points to first element it means, no time <= timestamp exists.
        return "" if right == 0 else self.key_time_map[key][right - 1][1]