class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        count = collections.Counter(nums)
        
        countList = []
        for k, v in count.items():
            countList.append((v, k))
        
        countList.sort(key = lambda x: [x[0],-x[1]])
        
        i = 0
        for freq, item in countList:
            stop = i + freq
            while i < stop:
                nums[i] = item
                i += 1
            
        return nums