# __author__ = 'iamkissg'
# __date__ = '20190921'


class Trie:

    '''
    对 Trie 完全不懂, 代码完全抄自覃超的算法课
    '''

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = {}
        self.end_of_word = '#'
        

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        node = self.root
        for c in word:
            # 如果 c 不在字典中, 插入一个 c: {} 的项
            # 然后再往下走一层
            node = node.setdefault(c, {})
        node[self.end_of_word] = self.end_of_word
        

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        node = self.root
        for c in word:
            if c not in node:
                return False
            node = node[c]
        else:
            return self.end_of_word in node


    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        node = self.root
        for c in prefix:
            if c not in node:
                return False
            node = node[c]
        else:
            return True
        


# Your Trie object will be instantiated and called as such:
obj = Trie()
obj.insert('iamkissg')
obj.insert('Google')
obj.insert('Apple')
obj.insert('Amazon')
obj.insert('Facebook')
obj.insert('Alibaba')
obj.insert('Tencent')
obj.insert('Mi')
print(obj.__dict__)
param_2 = obj.search('iamkissg')
param_3 = obj.startsWith('iam')