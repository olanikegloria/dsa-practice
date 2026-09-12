class Solution:
    def isHappy(self, n: int) -> bool:
        def next_num(x):
            s = 0
            while x:
                x, d = divmod(x, 10)
                s += d * d
            return s
        seen = set()
        while n not in seen:
            if n == 1:
                return True
            seen.add(n)
            n = next_num(n)
        return n == 1
