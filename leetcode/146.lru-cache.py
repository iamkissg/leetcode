class LRUCache:
    '''
    20190926
    用列表对 lru 进行计数
    执行用时 :728 ms, 在所有 Python3 提交中击败了11.03% 的用户
    内存消耗 :22.5 MB, 在所有 Python3 提交中击败了5.64%的用户
    '''

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.lru_counter = []
        self.lru = {}

    def update_lru(self, used_key):
        key_index = self.lru_counter.index(used_key)
        self.lru_counter.append(self.lru_counter.pop(key_index))

    def get(self, key: int) -> int:
        if key in self.lru:
            self.update_lru(key)
            return self.lru[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.lru:
            self.lru[key] = value
            self.update_lru(key)
        else:
            if len(self.lru) == self.capacity:
                key_to_remove = self.lru_counter.pop(0)
                self.lru.pop(key_to_remove)

            self.lru[key] = value
            self.lru_counter.append(key)
                

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
if __name__ == "__main__":
    obj = LRUCache(1101)
    for opt, val in zip(opts, values):
        if opt == 'put':
            obj.put(key=val[0], value=val[1])
        elif opt == 'get':
            obj.get(key=val[0])
