class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}
        for n in nums:
            if n not in counter:
                counter[n] = 0
            counter[n] += 1
        sorted_counter = sorted(counter.items(), key=lambda t: t[1], reverse=True)
        return [sorted_counter[i][0] for i in range(k)]