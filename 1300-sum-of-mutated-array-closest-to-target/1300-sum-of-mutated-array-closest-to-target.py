class Solution:
    def findBestValue(self, arr: List[int], target: int) -> int:
        arr.sort(reverse = True)
        maxElem = arr[0]
        n = len(arr)
        while arr and arr[-1] * len(arr) < target:
            target -= arr.pop()
        
        if not arr:
            return maxElem
        if target / len(arr) - target // len(arr) <= 0.5:
            return target // len(arr)
        return target // len(arr) + 1