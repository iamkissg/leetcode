from collections import Counter

class Solution:
    def isAnagram2(self, s: str, t: str) -> bool:
        '''排序法 执行用时：84 ms'''
        return sorted(s) == sorted(t)

    def isAnagram(self, s: str, t: str) -> bool:
        '''计数法 执行用时：60 ms'''
        return Counter(s) == Counter(t)

if __name__ == "__main__":
    sol = Solution()
    print(sol.isAnagram('art', 'ar'))
    print(sol.isAnagram('art', 'arttt'))
    print(sol.isAnagram('art', 'rta'))