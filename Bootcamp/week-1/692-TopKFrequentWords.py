class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        frequency_count = Counter(words)
        frequency_count = dict(sorted(frequency_count.items()))

        return nlargest(k, frequency_count.keys(), frequency_count.get)
