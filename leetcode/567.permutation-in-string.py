from collections import Counter



class Solution:
    def checkInclusion2(self, a: str, b: str) -> bool:
        '''
        20190929
        执行用时 :120 ms, 在所有 Python3 提交中击败了39.91% 的用户
        内存消耗 :13.9 MB, 在所有 Python3 提交中击败了5.11%的用户
        
        效率不一定最高, 不求有功, 但求无过, AC 就好
        '''
        counter_a = Counter(a)

        len_b = len(b)
        left, right = 0, len(a)-1
        tmp = Counter(b[left: right])
        need = {k: counter_a[k]-tmp.get(k, 0) for k in counter_a.keys()}
        while right < len_b:
            if b[right] in need:
                need[b[right]] -= 1
            
            if max(need.values()) <= 0:
                return True
            
            if b[left] in need:
                need[b[left]] += 1
            
            left += 1
            right += 1

        return False

    def checkInclusion(self, a: str, b: str) -> bool:
        '''
        20190930
        执行用时 :112 ms, 在所有 Python3 提交中击败了45.81% 的用户
        内存消耗 :13.7 MB, 在所有 Python3 提交中击败了5.11%的用户
        
        改成用 for-loop 自动维护右指针的做法
        '''

        len_a, len_b = len(a), len(b)
        if len_a > len_b:
            return False
        l = 0

        need = Counter(a)
        # r 从 len_a-1 开始, 是因为我们用的是双闭区间 [] 而不是 [)
        for r in range(len_a-1):
            if b[r] in need:
                need[b[r]] -= 1

        # 这是一个固定大小的窗口问题
        for r in range(len_a-1, len(b)):
            if b[r] in need:
                need[b[r]] -= 1

            if max(need.values()) <= 0:
                return True

            if b[l] in need:
                need[b[l]] += 1
            l += 1
            
        return False

if __name__ == "__main__":
    sol = Solution()
    print(sol.checkInclusion2(a="adc", b="dcda"))
    print(sol.checkInclusion(a="adc", b="dcda"))
    print(sol.checkInclusion2(a="ab", b="a"))
    print(sol.checkInclusion(a="ab", b="a"))
    print(sol.checkInclusion2(a="ab", b="eidbaooo"))
    print(sol.checkInclusion(a="ab", b="eidbaooo"))
    print(sol.checkInclusion2(a= "ab", b="eidboaoo"))
    print(sol.checkInclusion(a= "ab", b="eidboaoo"))