from typing import List


class Solution:

    def __init__(self):
        self.mapping = {
            '1': '1',
            '6': '9',
            '8': '8',
            '9': '6',
            '0': '0',
        }

    def findStrobogrammatic(self, n: int) -> List[str]:
        if n == 0:
            return []
        if n == 1:
            return ["0", "1", "8"]
        if n == 2:
            return ["11","69","88","96"]

        res = ["0", "1", "8"] if n & 1 else ["11","69","88","96", "00"]
        start = 1 if n & 1 else 2
        for i in range(start, n, 2):
            res = [k+c+v for c in res for k, v in self.mapping.items()]

        # print(res)
        return list(filter(lambda t: not t.startswith('0'), res))

if __name__ == "__main__":
    sol = Solution()
    print(sol.findStrobogrammatic(1))
    print(sol.findStrobogrammatic(2))
    print(sol.findStrobogrammatic(3))