from collections import Counter


class Solution(object):
    def frequencySort(self, s):
        """
        20191019

        同样的代码, 执行两次, 结果大不相同, 我看出差别了, Python 和 Python3
        36 ms	14.9 MB	Python3
        56 ms	14.1 MB	Python
        """
        if not s:
            return ""
        
        counter = Counter(s)
        res = ''
        for k, v in sorted(counter.items(), key=lambda t: t[1], reverse=True):
            res += k * v
        return res
