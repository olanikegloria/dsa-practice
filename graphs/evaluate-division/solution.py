from typing import List
from collections import defaultdict, deque

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(dict)
        for (a, b), v in zip(equations, values):
            graph[a][b] = v
            graph[b][a] = 1.0 / v

        def bfs(src, dst):
            if src not in graph or dst not in graph:
                return -1.0
            if src == dst:
                return 1.0
            q = deque([(src, 1.0)])
            seen = {src}
            while q:
                node, cur = q.popleft()
                for nxt, w in graph[node].items():
                    if nxt in seen:
                        continue
                    nval = cur * w
                    if nxt == dst:
                        return nval
                    seen.add(nxt)
                    q.append((nxt, nval))
            return -1.0

        return [bfs(a, b) for a, b in queries]
