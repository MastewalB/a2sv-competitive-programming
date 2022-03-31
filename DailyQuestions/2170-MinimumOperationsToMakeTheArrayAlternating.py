class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        even_counter = defaultdict(int)
        odd_counter = defaultdict(int)

        for i in range(len(nums)):
            if i % 2 == 0:
                even_counter[nums[i]] += 1
            else:
                odd_counter[nums[i]] += 1

        even_counter = sorted(even_counter.items(),
                              key=lambda x: x[1], reverse=True)
        odd_counter = sorted(odd_counter.items(),
                             key=lambda x: x[1], reverse=True)

        if even_counter[0][0] != odd_counter[0][0]:
            return len(nums) - (even_counter[0][1] + odd_counter[0][1])

        even = even_counter[0][1] + \
            odd_counter[1][1] if len(odd_counter) > 1 else even_counter[0][1]
        odd = odd_counter[0][1] + \
            even_counter[1][1] if len(even_counter) > 1 else odd_counter[0][1]

        return len(nums) - max(even, odd)
