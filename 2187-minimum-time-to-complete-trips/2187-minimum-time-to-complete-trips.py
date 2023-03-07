class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        time.sort()
        left = time[0]
        right = time[0] * totalTrips
        # print(self.calcTrip(time, 4))
        
        while left <= right:
            mid = left + (right - left) // 2
            if self.calcTrip(time, mid) < totalTrips:
                left = mid + 1
            else:
                right = mid - 1
        return left
        
        
    def calcTrip(self, times, time):
        trips = 0
        for i in times:
            trips += time // i
        return trips