class Solution:
    def romanToInt(self, s: str) -> int:
        dic = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        
        if len(s) == 1:
            return dic[s]
        
        res = 0
        i = 0
        while i < len(s) - 1:
            if dic[s[i]] < dic[s[i+1]]:
                res += dic[s[i+1]] - dic[s[i]]
                i += 2
            else:
                print(res, s[i])
                res += dic[s[i]]
                i += 1
        if i == len(s)-1:
            res += dic[s[i]]
        
        return res

if __name__ == "__main__":
    sol = Solution()
    print(sol.romanToInt('III'))
    print(sol.romanToInt('IV'))
    print(sol.romanToInt('IX'))
    print(sol.romanToInt('LVIII'))
    print(sol.romanToInt('MCMXCIV'))