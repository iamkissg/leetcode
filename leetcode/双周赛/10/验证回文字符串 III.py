class Solution:
    def __init__(self):
        self.memo = {}

    def isValidPalindrome(self, s: str, k: int) -> bool:
        n = len(s)

        if k < 0:
            return False
        hash = s+':'+str(k)
        if hash in self.memo:
            return self.memo[hash]
        if n <= 1:
            return True
        if s == s[::-1]:
            self.memo[s+':'+str(k)] = True
            return True
    
        l, r = 0, n-1
        if s[l] == s[r]:
            self.memo[s[l+1:r]+':'+str(k)] = self.isValidPalindrome(s[l+1:r], k)
            return self.memo[s[l+1:r]+':'+str(k)]
        else:
            # self.memo[s[l+1:r]+':'+str(k-2)] = self.isValidPalindrome(s[l+1:r], k-2)
            # if self.memo[s[l+1:r]+':'+str(k-2)]:
            #     return True
            self.memo[s[l+1:r+1]+':'+str(k-1)] = self.isValidPalindrome(s[l+1:r+1], k-1)
            if self.memo[s[l+1:r+1]+':'+str(k-1)]:
                return True
            self.memo[s[l:r]+':'+str(k-1)] = self.isValidPalindrome(s[l:r], k-1)
            if self.memo[s[l:r]+':'+str(k-1)]:
                return True
            return False
            # return self.memo[s[l+1:r+1]+':'+str(k-1)] or self.memo[s[l:r]+':'+str(k-1)] or self.memo[s[l+1:r]+':'+str(k-2)]


if __name__ == "__main__":
    sol = Solution()
    print(sol.isValidPalindrome(s = "abcqdeca", k = 2))
    print(sol.isValidPalindrome("fcgihcgeadfehgiabegbiahbeadbiafgcfchbcacedbificicihibaeehbffeidiaiighceegbfdggggcfaiibefbgeegbcgeadcfdfegfghebcfceiabiagehhibiheddbcgdebdcfegaiahibcfhheggbheebfdahgcfcahafecfehgcgdabbghddeadecidicchfgicbdbecibddfcgbiadiffcifiggigdeedbiiihfgehhdegcaffaggiidiifgfigfiaiicadceefbhicfhbcachacaeiefdcchegfbifhaeafdehicfgbecahidgdagigbhiffhcccdhfdbd",
                                216))
    print(sol.isValidPalindrome("acbbbcaaadbdddcbbaabdabbdbaadcadadaadcdbabbcbbbcaadaaddcbdcaabdbacdcdccbaaadcdbadbbbcbbbddbadcacbacbaacdbddcbcadddadadbabdaacbdacdbcccbcbadbacdbaaadbcbddbbabcdccaccabbabdcadaddbadbccdddccbdbdacabbcbbbcadcdadaadbdaaad",
                                216))
    print(sol.isValidPalindrome("dadaabbdddcabbccdcaabadbbcccbacdcacacbdbabbadcdabacbadcdabcbbaacdabbdcbabdcbbbcaddccbdbbaaadcbaabaadbadcdadcdcddddcdbbddcbddbbdbabababcbdabddabcdcbcaaaacbbbdcbabbbcaacbcbacaaabccdbdddbbcbbbcacacbbdccacacddaabccbaccddcbdcbcacadbaacccbaabaccdaddbdadcccbbbcbbbdcbbacacbabdcddcbbbccdcbbabddcbbabbacdcadcaaddcdcdaaccadbcdacbbdccaccdaaaabbcdcadddadcddbdccadabcbbadbbdbbaccbdadbdbbdcaccccccaddaaacbadcbbacbbbddacbadbdabdcbcacadbcdabbdbaddcdcabbbbabbacdacbacdaccbcbbcaccbabcbdbaccacddccdbabcbaadadacadabacddadadcbdaacdbd",
                                216))