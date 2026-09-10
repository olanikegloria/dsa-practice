from typing import List

class Codec:
    def encode(self, strs: List[str]) -> str:
        return "".join(f"{len(s)}#{s}" for s in strs)

    def decode(self, s: str) -> List[str]:
        out: List[str] = []
        i = 0
        while i < len(s):
            j = s.index("#", i)
            size = int(s[i:j])
            start = j + 1
            out.append(s[start:start + size])
            i = start + size
        return out


class Solution:
    def build(self) -> Codec:
        return Codec()
