from collections import Counter
from string import ascii_uppercase, ascii_lowercase, digits, ascii_letters
import re

class Solution:
    ''''''
    def unfold_formula(self, s, i):
        result = ''
        count = 0
        while i >= 0:
            if s[i] in digits:
                j = i+1
                while s[i-1] in digits:
                    i -= 1
                count = int(s[i: j])
            elif s[i] == ')':
                sub_str, i = self.unfold_formula(s, i-1)
                result += sub_str * count
                count = 0
            elif s[i] == '(':
                return result, i
            elif s[i] in ascii_letters:
                if s[i] in ascii_lowercase:
                    result += s[i-1:i+1] * (count if count else 1)
                    i -= 1
                else:
                    result += s[i] * (count if count else 1)
                count = 0
            i -= 1
        return result

    def countOfAtoms(self, formula: str) -> str:
        '''
        20190928
        超出时间限制	N/A	N/A	Python3, 24/28
        相对来说比较暴力的解法, 把化学方程式展开, 然后数每个元素的个数
        '''
        
        result = self.unfold_formula(formula, len(formula)-1)
        # length = len(result)
        # counter = {}
        # i = 0
        counter = Counter(re.findall(r'[A-Z][a-z]|[A-Z]', result))
        # while i < length:
        #     if i < length-1 and result[i+1] in ascii_lowercase:
        #         if result[i: i+2] not in counter:
        #             counter[result[i: i+2]] = 0
        #         counter[result[i: i+2]] += 1
        #         i += 2
        #     else:
        #         if result[i] not in counter:
        #             counter[result[i]] = 0
        #         counter[result[i]] += 1
        #         i += 1

        d = ''.join([k+str(v) if v > 1 else k for k, v in sorted(counter.items())])
        return d



if __name__ == "__main__":
    sol = Solution()
    # print(sol.countOfAtoms(""))
    print(sol.countOfAtoms("H50"))
    print(sol.countOfAtoms("Be32"))
    print(sol.countOfAtoms("H2O"))
    print(sol.countOfAtoms("Mg(OH)2"))
    print(sol.countOfAtoms("K4(ON(SO3)2)2"))  # "K4N2O14S4"
    print(sol.countOfAtoms("(((U42Se42Fe10Mc31Rh49Pu49Sb49)49V39Tm50Zr44Og6)33((W2Ga48Tm14Eu46Mt12)23(RuRnMn11)7(Yb15Lu34Ra19CuTb2)47(Md38BhCu48Db15Hf12Ir40)7CdNi21(Db40Zr24Tc27SrBk46Es41DsI37Np9Lu16)46(Zn49Ho19RhClF9Tb30SiCuYb16)15)37(Cr48(Ni31)25(La8Ti17Rn6Ce35)36(Sg42Ts32Ca)37Tl6Nb47Rh32NdGa18Cm10Pt49(Ar37RuSb30Cm32Rf28B39Re7F36In19Zn50)46)38(Rh19Md23No22PoTl35Pd35Hg)41)50"))  # "K4N2O14S4"