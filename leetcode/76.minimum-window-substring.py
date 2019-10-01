from collections import Counter

class Solution:
    def minWindow2(self, s: str, t: str) -> str:
        '''
        20190929
        题设的要求是, 不仅要包含所有的字母, 而且字母个数也要符合要求
        执行用时 :1524 ms, 在所有 Python3 提交中击败了6.02% 的用户
        内存消耗 :14.6 MB, 在所有 Python3 提交中击败了15.00%的用户

        滑动窗口的思想我明白, 但是边界问题还是处理不好
        把 win 替换成 need, 检查窗口是否合法的效率上有所提高 (5 倍), 但还是差了点啊
        执行用时 :320 ms, 在所有 Python3 提交中击败了32.13% 的用户
        内存消耗 :14.5 MB, 在所有 Python3 提交中击败了15.00%的用户
        '''
        if not s or not t:
            return ''

        counter_s = Counter(s)
        counter_t = Counter(t)
        if not all(counter_s[k] >= counter_t[k] for k in counter_t.keys()):
            return ''

        len_s, len_t = len(s), len(t)
        left, right = 0, 0
        result = s
        # win = Counter(s[left: right])
        need = {k: v for k, v in counter_t.items()}
        while right < len_s:
            # if win.keys() < counter_t.keys() or not all(win[k] >= counter_t[k] for k in counter_t.keys()):
                # win[s[right]] = win.setdefault(s[right], 0) + 1
            if max(need.values()) > 0:
                if s[right] in need:
                    need[s[right]] -= 1
                right += 1

            # while all(win[k] >= counter_t[k] for k in counter_t.keys()):
            while max(need.values()) <= 0:
                result = s[left: right] if not result or len(s[left: right]) < len(result) else result
                # win[s[left]] -= 1
                if s[left] in need:
                    need[s[left]] += 1
                left += 1
        return result


    def minWindow(self, s: str, t: str) -> str:
        '''
        20190930
        执行用时 :260 ms, 在所有 Python3 提交中击败了37.99% 的用户
        内存消耗 :14.5 MB, 在所有 Python3 提交中击败了15.00%的用户

        重写了下, 改用 for-loop 控制右指针
        '''
        if not s or not t:
            return ''

        counter_s = Counter(s)
        counter_t = Counter(t)
        if not all(counter_s.get(k, 0) >= counter_t[k] for k in counter_t.keys()):
            return ''

        len_s, len_t = len(s), len(t)
        l = 0
        result = s
        need = {k: v for k, v in counter_t.items()}
        for r in range(len_s):
            if s[r] in need:
                need[s[r]] -= 1

            # 窗口符合要求, 移动左指针
            while max(need.values()) <= 0:
                if len(s[l: r+1]) < len(result):
                    result = s[l: r+1]

                if s[l] in need:
                    need[s[l]] += 1
                l += 1
        return result



if __name__ == "__main__":
    sol = Solution()
    print(sol.minWindow(s = "ab", t = "a"))
    print(sol.minWindow(s = "bbaa", t = "aba"))
    print(sol.minWindow(s = "A", t = "A"))
    print(sol.minWindow(s = "ADOBECODEBANC", t = "ABC"))
    print(sol.minWindow(s = "ADOBECODEBANC", t = "ABO"))
    print(sol.minWindow(s = "", t = "ABO"))
    print(sol.minWindow(s = "", t = ""))
    print(sol.minWindow(s = "AB", t = "ABC"))
    print('#'*40)
    print(sol.minWindow2(s = "ab", t = "a"))
    print(sol.minWindow2(s = "bbaa", t = "aba"))
    print(sol.minWindow2(s = "A", t = "A"))
    print(sol.minWindow2(s = "ADOBECODEBANC", t = "ABC"))
    print(sol.minWindow2(s = "ADOBECODEBANC", t = "ABO"))
    print(sol.minWindow2(s = "", t = "ABO"))
    print(sol.minWindow2(s = "", t = ""))
    print(sol.minWindow2(s = "AB", t = "ABC"))