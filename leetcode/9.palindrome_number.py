class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        if x < 10:
            return True
        else:
            strx = str(x)
            lenx = len(strx)
            for i in range(lenx//2):
                if strx[i] != strx[lenx-i-1]:
                    return False
            else:
                return True
        