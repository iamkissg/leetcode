class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        '''
        20190930
        执行用时 :360 ms, 在所有 Python3 提交中击败了31.73% 的用户
        内存消耗 :13.9 MB, 在所有 Python3 提交中击败了5.00%的用户
        自己失败了太多次了, 问题是, 思路就是错了.
        以下是网友的题解, 对我的滑动窗口写法挺有启发性的:

        1. 让 for-loop 自动维护一个右指针就行了, 反正右指针永远向后, 直到数组/字符串的末尾
            1. 用 for-loop 自动维护右指针的一个好处是, 消除了我心中对右指针何时更新及边界的困扰
        2. 我一直纠结于以滑动窗口内的最左端还是出现次数最多的元素更新 k, 看来都想错了 (我说怎么都不对)
            1. 替换次数确定了之后, 另一点好处是, 何时移动左指针, 网友的做法就清晰多了, 当替换的超过了 k, 不像我最初纠结于 k 要不要等于 0
        3. max 和 sorted 一样, 也带 key 关键字, 而且对于字典的 max, 用 letter.get 作为 key, 太有用了 (类似 argmax)
        4. 以后不用另写 if 语句判断字典中是否存在某 key, 只要 d.get(key, 0) 即可
        '''

        # 用字典保存字母出现的次数，需要替换的字符数目＝窗口字符数目－数量最多的字符数目
        letter_num = {}
        l = 0
        res = 0
        for r in range(len(s)):
            # 字典保存字符出现的次数
            letter_num[s[r]] = letter_num.get(s[r], 0) + 1
            # 找到出现次数最多的字符
            max_letter = max(letter_num, key=letter_num.get)

            # 如果替换的字符数目超过给定的k，则移动左边界
            while r - l + 1 - letter_num[max_letter] > k:
                letter_num[s[l]] -= 1
                l += 1
                # 需要更新最多个数的字符
                max_letter = max(letter_num, key=letter_num.get)

            # 如果s[r] 超出了替换的字符数目，需要先处理，再计算结果
            res = max(res, r - l + 1)
            
        return res
                


if __name__ == "__main__":
    sol = Solution()
    print(sol.characterReplacement(s = "BAAA", k = 2))
    print(sol.characterReplacement(s = "BAAA", k = 0))
    print(sol.characterReplacement(s = "AAAA", k = 2))
    print(sol.characterReplacement(s = "AAAB", k = 0))
    print(sol.characterReplacement(s = "ABAB", k = 1))
    print(sol.characterReplacement(s = "ABAB", k = 2))
    print(sol.characterReplacement(s = "AABABBA", k = 1))