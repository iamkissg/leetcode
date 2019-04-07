class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if not (a or b):
            raise ValueError('Empty string.')

        return bin(int(a, 2) + int(b, 2))[2:]


if __name__ == "__main__":
    sol = Solution()
    print(sol.addBinary('11', '1'))
    print(sol.addBinary('1010', '1011'))
    print(sol.addBinary('1010', '0'))
    print(sol.addBinary('1010', ''))
    print(sol.addBinary('1010', ''))
    print(sol.addBinary('', '1'))
    print(sol.addBinary('', ''))
