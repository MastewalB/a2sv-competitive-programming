class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        self.persons = persons
        self.times = times
        self.votes = []
        self.get_leading_vote()
        print(self.votes)

    def q(self, t: int) -> int:
        left, right = 0, len(self.times) - 1

        while left <= right:
            mid = left + (right - left) // 2
            if self.times[mid] == t:
                return self.votes[mid]
            elif self.times[mid] < t:
                left = mid + 1
            else:
                right = mid - 1
        return self.votes[left - 1]

    def get_leading_vote(self):
        count = Counter()
        lead = -1
        for person in self.persons:
            count[person] += 1
            if count[person] >= count[lead]:
                lead = person
            self.votes.append(lead)

# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)
