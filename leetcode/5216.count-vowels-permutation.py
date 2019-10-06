from queue import deque


class Solution:

    mapping = {
        'a': ['e'],
        'e': ['a', 'i'],
        'i': ['a', 'e', 'o', 'u'],
        'o': ['i', 'u'],
        'u': ['a'],
    }
    MOD = 10**9 + 7

    def countVowelPermutation(self, n: int) -> int:
        '''
        20191005

        696 ms	14 MB	Python3

        157 周赛的第四题, 这里我只记录末尾元音的个数, 然后据此推断下一轮元音数量的变化, 同样只记录末位的情况
        依据是, 增加元音时, 增加的元音只和末位有关
        总数则对不同元音结尾的总数求和即可
        '''
        if n <= 0:
            return 0

        res = {'a': 1,'e': 1,'i': 1,'o': 1,'u': 1}

        for i in range(n-1):
            new_res = {k: 0 for k in res}
            for s in res:
                for c in self.mapping[s]:
                    new_res[c] += res[s]
            res = new_res
            
        return sum(res.values()) % self.MOD


if __name__ == "__main__":
    sol = Solution()
    print(sol.countVowelPermutation(1))
    print(sol.countVowelPermutation(2))
    print(sol.countVowelPermutation(3))
    print(sol.countVowelPermutation(5))