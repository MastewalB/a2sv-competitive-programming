class Solution_One:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        left = 0
        right = len(people) - 1
        boats = 0
        carry = 0

        while left < right:
            if carry + people[left] + people[right] > limit:
                if carry > 0:
                    boats += 1
                    carry = 0
                    right -= 1
                    continue
                boats += 1
                right -= 1
            elif carry + people[left] + people[right] < limit:
                carry += people[left]
                left += 1
            else:
                if carry > 0:
                    carry = 0
                boats += 1
                left += 1
                right -= 1
        if left == right:
            boats += 1
        return boats


class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        left = 0
        right = len(people) - 1
        boats = 0

        while left < right:
            if people[left] + people[right] > limit:
                boats += 1
                right -= 1
            else:
                boats += 1
                left += 1
                right -= 1
        if left == right:
            boats += 1
        return boats
