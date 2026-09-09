from collections import defaultdict, deque
from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        indegree = [0] * numCourses
        for course, need in prerequisites:
            graph[need].append(course)
            indegree[course] += 1
        q = deque(i for i, d in enumerate(indegree) if d == 0)
        seen = 0
        while q:
            cur = q.popleft()
            seen += 1
            for nxt in graph[cur]:
                indegree[nxt] -= 1
                if indegree[nxt] == 0:
                    q.append(nxt)
        return seen == numCourses
