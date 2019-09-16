class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        if not text:
            return 0

        counter = {}
        for w in text:
            if w not in counter:
                counter[w] = 0
            counter[w] += 1

        return min([counter.get(w, 0) // 2 if w in ('l', 'o') else counter.get(w, 0) for w in 'balon'])


if __name__ == "__main__":
    sol = Solution()
    print(sol.maxNumberOfBalloons(''))
    print(sol.maxNumberOfBalloons('n'))
    print(sol.maxNumberOfBalloons('nlaebolko'))
    print(sol.maxNumberOfBalloons('loonbalxballpoon'))
    print(sol.maxNumberOfBalloons('leetcode'))