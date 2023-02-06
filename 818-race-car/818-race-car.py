class Solution:
    def racecar(self, target: int) -> int:
        Q = collections.deque([(0, 1)])
        visited = set([(0, 1)])
        steps = 0
        while Q:
            for _ in range(len(Q)):
                pos, speed = Q.popleft()
                if pos == target:
                    return steps
                if not (pos+speed, speed*2) in visited:
                    Q.append((pos+speed, speed*2))
                    visited.add((pos+speed, speed*2))
                if not (pos, -1 if speed > 0 else 1) in visited:
                    Q.append((pos, -1 if speed > 0 else 1))
                    visited.add((pos, -1 if speed > 0 else 1))
            steps += 1