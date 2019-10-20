from typing import List

class Trie:
    def __init__(self):
        self.root = {}

    def insert(self, s):
        node = self.root
        for c in s:
            node = node.setdefault(c, {})
        node['#'] = '#'


class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        trie = Trie()

        folder = sorted(folder)
        # parents = set()
        for f in folder:
            trie.insert(f.split('/'))
        
        
        res = self.dfs(trie.root)

        return [item.rstrip('/') for item in res]
    
    def dfs(self, root):
        if '#' in root.keys():
            return ['']

        res = []
        for k, v in root.items():
            returned = self.dfs(v)
            res.extend([k+'/'+item for item in returned])
        
        return res


if __name__ == "__main__":
    sol = Solution()
    print(sol.removeSubfolders(["/a","/a/b","/c/d","/c/d/e","/c/f"]))
    print(sol.removeSubfolders(["/a","/a/b/c","/a/b/d"]))
    print(sol.removeSubfolders(["/a/b/c","/a/b/d","/a/b/ca"]))