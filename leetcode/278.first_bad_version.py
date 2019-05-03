# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool

def isBadVersion(version: int):
    pass

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        if not isinstance(n, int) or n < 1:
            raise ValueError
        if n == 1:
            if isBadVersion(1):
                return 1
            else:
                return 0
        start = 0
        end = n
        mid = end
        while start + 1 != end:
            # first bad version is this or previous
            if isBadVersion(mid):
                end = mid
            else:
                start = mid
            mid = (start + end) // 2
        # else:
        #     if not isBadVersion(start):
        #         return start
        #     else:
        #         return end
        return end