from typing import List

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        out: List[List[str]] = []
        path: List[str] = []

        def is_pal(lo: int, hi: int) -> bool:
            while lo < hi:
                if s[lo] != s[hi]:
                    return False
                lo += 1
                hi -= 1
            return True

        def dfs(start: int) -> None:
            if start == len(s):
                out.append(path[:])
                return
            for end in range(start, len(s)):
                if is_pal(start, end):
                    path.append(s[start:end + 1])
                    dfs(end + 1)
                    path.pop()

        dfs(0)
        return out
