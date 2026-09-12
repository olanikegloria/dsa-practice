class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        def transform(src, dst):
            m = {}
            for a, b in zip(src, dst):
                if a in m:
                    if m[a] != b:
                        return False
                elif b in m.values():
                    return False
                else:
                    m[a] = b
            return True
        return transform(s, t)
