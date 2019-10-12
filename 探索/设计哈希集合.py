class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.MOD = 1000000
        self.hashset = []
        

    def add(self, key: int) -> None:
        if not self.contains(key):
            self.hashset.append(key % self.MOD)

        

    def remove(self, key: int) -> None:
        if self.contains(key):
            self.hashset.remove(key%self.MOD)
        

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        return key%self.MOD in self.hashset
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)