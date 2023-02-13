class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:

        count, total = defaultdict(int), 0
        count[0] += 1
        S = 0

        for n in nums:
            total += n
            r = total % k
            S += count[r]
            count[r] += 1
        
        return S