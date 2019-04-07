class Solution:
    
    def __init__(self):
        seqs = ['1']
        for i in range(2, 31):
            seq = seqs[-1]
            new_seq = []
            count = 0
            pre_t = ''
            for t in seq:
                if count == 0:
                    pre_t = t
                    count += 1
                else:
                    if t == pre_t:
                        count += 1
                    else:
                        new_seq.append(str(count)+pre_t)
                        count = 1
                        pre_t = t
            else:
                new_seq.append(str(count)+pre_t)
            seqs.append(''.join(new_seq))
        self.seqs = seqs

    def countAndSay(self, n: int) -> str:
        return self.seqs[n-1]



if __name__ == "__main__":
    sol = Solution()
    print(sol.countAndSay(1))
    print(sol.countAndSay(2))
    print(sol.countAndSay(3))
    print(sol.countAndSay(4))
    print(sol.countAndSay(5))
    print(sol.countAndSay(6))
    print(sol.countAndSay(7))
    print(sol.countAndSay(8))
    print(sol.countAndSay(9))
    print(sol.countAndSay(10))
    print(sol.countAndSay(11))