class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(set)
        inDeg = defaultdict(int)
        queue = deque()
        
        for course, pre in prerequisites:
            graph[pre].add(course)
            inDeg[course] += 1
            
        
        for course in range(numCourses):
            if inDeg[course] == 0:
                queue.append(course)
        
        processedCount = 0
        while queue:
            course = queue.popleft()
            processedCount += 1
            
            for neighCourse in graph[course]:
                inDeg[neighCourse] -= 1
                if inDeg[neighCourse] == 0:
                    queue.append(neighCourse)
        
        return processedCount == numCourses
        
        