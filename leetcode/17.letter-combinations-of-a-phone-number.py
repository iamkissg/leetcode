from typing import List


class Solution:
    mapping = {
        '2': ['a', 'b', 'c'],
        '3': ['d', 'e', 'f'],
        '4': ['g', 'h', 'i'],
        '5': ['j', 'k', 'l'],
        '6': ['m', 'n', 'o'],
        '7': ['p', 'q', 'r', 's'],
        '8': ['t', 'u', 'v'],
        '9': ['w', 'x', 'y', 'z'],
    }
    def letterCombinations(self, digits: str) -> List[str]:
        '''
        20191005
        60 ms	13.8 MB	Python3

        本题没什么滑头呀, 不过要注意, res 在前, mapping 在后
        '''
        if not digits:
            return []

        res = ['']
        for n in digits:
            res = [s+c for s in res for c in self.mapping[n]]
        return res

if __name__ == "__main__":
    sol = Solution()
    print(sol.letterCombinations('23'))
    print(sol.letterCombinations('23'))
    print(sol.letterCombinations('234'))
