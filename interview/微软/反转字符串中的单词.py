class Solution:
    def reverseWords(self, s: str) -> str:
        '''
        20191015
        Python 一行代码版
        '''
        # return ' '.join(s.split()[::-1])

        '''
        20191015
        两次反转法
        '''
        reversed_s = s[::-1]
        return ' '.join(c[::-1] for c in reversed_s.strip().split())