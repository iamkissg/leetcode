from typing import List


class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        '''
        20190928
        答案来自 Leetcode-cn 上网友的题解
        '''
        # 这里很有技巧性, arr 和 A 的位置是一一对应的,
        # 每个元素都是一个字典, 用于记录以当前位置的元素为等差数列的队尾, 不同等差数列的长度
        arr = [{} for i in range(len(A))]
        for i in range(1, len(A)):
            for j in range(i):
                # j 在 i 之前
                d = A[i] - A[j]          # 差
                # 这一步也很有技巧性, 查看数组中, 到 A[j] 的差为 d 的等差队列的长度,
                # get 的默认值是 1, 即不存在以 A[j] 为队列尾的等差队列, 因此只有一个 A[j],
                # +1 表示加上自身 A[i]
                n = arr[j].get(d,1) + 1
                arr[i][d] = n
        
        max_len = max([v for d in arr for k, v in d.items()])
        return max_len


if __name__ == "__main__":
    sol = Solution()
    print(sol.longestArithSeqLength([3,6,9,12]))
    
