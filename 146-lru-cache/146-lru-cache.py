class Node:
    def __init__(self,key,val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None
        
class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.hashmap = {}  #map key to node
        self.LRU = Node(0,0)
        self.MRU = Node(0,0) #MRU = most recently used
        self.LRU.next = self.MRU
        self.MRU.prev = self.LRU
        
    def remove(self,node):
        prev = node.prev
        nxt  = node.next
        
        prev.next = nxt
        nxt.prev = prev
        
    def insert(self,node):
        prev = self.MRU.prev
        nxt  = self.MRU
        
        prev.next = nxt.prev = node
        node.prev,node.next = prev,nxt
        

    def get(self, key: int) -> int:
        if key in self.hashmap:
            self.remove(self.hashmap[key])
            self.insert(self.hashmap[key])
            
            return self.hashmap[key].val
        return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.hashmap:
            self.remove(self.hashmap[key])
        
        self.hashmap[key] = Node(key,value)
        self.insert(self.hashmap[key]) #because now it has become MRU
        if len(self.hashmap)>self.cap:
            
            lru = self.LRU.next
            self.remove(lru)
            del self.hashmap[lru.key]
        
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)