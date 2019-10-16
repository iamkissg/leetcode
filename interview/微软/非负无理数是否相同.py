import re


class Solution:
    pattern = r'\(\d*\)'
    def isRationalEqual(self, S: str, T: str) -> bool:
        recurrent_in_S = re.findall(self.pattern, S)
        if recurrent_in_S:
            recurrent_in_S = recurrent_in_S[0][1:-1]
            replaced_S = re.sub(self.pattern, recurrent_in_S*64, S)[:64]
        else:
            replaced_S = S

        recurrent_in_T = re.findall(self.pattern, T)
        if recurrent_in_T:
            recurrent_in_T = recurrent_in_T[0][1:-1]
            replaced_T = re.sub(self.pattern, recurrent_in_T*64, T)[:64]
        else:
            replaced_T = T

        float_S = float(replaced_S)
        float_T = float(replaced_T)
        print(float_S, float_T, abs(float_S-float_T))
        return abs(float_S-float_T) < 1e-9

if __name__ == "__main__":
    sol = Solution()
    print(sol.isRationalEqual(S = "0.(52)", T = "0.5(25)"))
    print(sol.isRationalEqual(S = "0.1666(6)", T = "0.166(66)"))
    print(sol.isRationalEqual(S = "0.9(9)", T = "1."))
    print(sol.isRationalEqual("8.123(4567)", "8.123(4566)"))