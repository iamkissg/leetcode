class Solution:
    def licenseKeyFormatting(self, S: str, K: int) -> str:
        '''
        20191010
        48 ms	14.5 MB	Python3
        '''
        reverse_string = ''.join(S.split('-'))[::-1]

        ans = '-'.join([reverse_string[i: i+K] for i in range(0, len(reverse_string), K)])
        return ans[::-1].upper()

if __name__ == "__main__":
    sol = Solution()
    print(sol.licenseKeyFormatting(S = "5F3Z-2e-9-w", K = 4))
    print(sol.licenseKeyFormatting(S = "2-5g-3-J", K = 2))
