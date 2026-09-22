from typing import List
from collections import deque

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        dead = set(deadends)
        if "0000" in dead:
            return -1
        q = deque([("0000", 0)])
        seen = {"0000"}
        while q:
            state, turns = q.popleft()
            if state == target:
                return turns
            for i in range(4):
                digit = int(state[i])
                for d in (-1, 1):
                    nd = (digit + d) % 10
                    nxt = state[:i] + str(nd) + state[i + 1 :]
                    if nxt not in seen and nxt not in dead:
                        seen.add(nxt)
                        q.append((nxt, turns + 1))
        return -1
