class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hashmap = [None for _ in range(1000000)]
    
    def hash_func(self, key):
        return key % 1000000
        

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        mapped_key = self.hash_func(key)
        self.hashmap[mapped_key] = value

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        mapped_key = self.hash_func(key)
        return -1 if self.hashmap[mapped_key] is None else self.hashmap[mapped_key]
        

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        mapped_key = self.hash_func(key)
        self.hashmap[mapped_key] = None
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)