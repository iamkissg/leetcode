class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        if len(haystack) < len(needle):
            return -1
        if len(haystack) == len(needle):
            return 0 if haystack == needle else -1
        
        len_needle = len(needle)
        for i in range(len(haystack)-len(needle)+1):
            if haystack[i:i+len_needle] == needle:
                return i
        else:
            return -1


if __name__ == "__main__":
    sol = Solution()
    print(sol.strStr('hello', 'll'))
    print(sol.strStr('hello', ''))
    print(sol.strStr('hello', 'h'))
    print(sol.strStr('hello', 'o'))
    print(sol.strStr('aaaaaa', 'ba'))
    print(sol.strStr('a', 'a'))
    print(sol.strStr('mississippi', 'pi'))