class MyHashSet:
    '''
    20191011
    1992 ms	18.2 MB	Python3
    '''

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hashset = []
    
    def hash_func(self, key):
        return key % 1000000

    def add(self, key: int) -> None:
        if not self.contains(key):
            self.hashset.append(self.hash_func(key))

        

    def remove(self, key: int) -> None:
        if self.contains(key):
            self.hashset.remove(self.hash_func(key))
        

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        return self.hash_func(key) in self.hashset
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)