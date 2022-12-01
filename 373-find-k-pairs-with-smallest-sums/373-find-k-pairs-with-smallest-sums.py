class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        answer = []
        visited = set((0, 0))
        heap = [(nums1[0] + nums2[0],0, 0)]
        
        while len(answer) < k and heap:
            
            s, i, j = heapq.heappop(heap)
            answer.append([nums1[i], nums2[j]])
            
            if i < len(nums1) - 1 and (i + 1, j) not in visited:
                visited.add((i + 1, j))
                heapq.heappush(heap, (nums1[i + 1] + nums2[j],i + 1, j))
            if j < len(nums2) - 1 and (i, j + 1) not in visited:
                visited.add((i, j + 1))
                heapq.heappush(heap, (nums1[i] + nums2[j + 1],i, j + 1))
        
        return answer