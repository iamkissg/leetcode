from collections import OrderedDict


class LRUCache(OrderedDict):
    '''
    20190926
    用列表对 lru 进行计数
    216 ms	23 MB	Python3
    '''

    def __init__(self, capacity: int):
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key in self:
            # last=True, 将当前项移到字典末尾
            # last=False, 将当前项移到字典开头
            self.move_to_end(key, last=True)
            return self[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self:
            self.move_to_end(key, last=True)
        self[key] = value
        if len(self) > self.capacity:
            # last=False 时, 采用 FIFO 的机制, 将先进来的项移除字典
            # last=True 时, 采用 LIFO 的机制
            self.popitem(last=False)
                

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)