class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], persons: List[int]) -> List[int]:
        bloom = defaultdict(int)
        answer = [0] * len(persons)
        
        for start, end in flowers:
            bloom[start] += 1
            bloom[end + 1] -= 1
        
        B = list(bloom.keys())
        B.sort()
        # print(B)
        
        prev = bloom[B[0]]
        for i in range(1, len(B)):
            bloom[B[i]] += prev
            prev = bloom[B[i]]
        
        
        for i in range(len(persons)):
            left, right = 0, len(B) - 1
            P = persons[i]
            
            while left <= right:
                
                mid = (left + right) >> 1
                if B[mid] <= P:
                    left = mid + 1
                else:
                    right = mid - 1
            
            answer[i] = bloom[B[right]]
            

        return answer 
            