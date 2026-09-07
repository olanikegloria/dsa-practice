class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = [0] * 26
        left = best = maxf = 0
        for right, ch in enumerate(s):
            idx = ord(ch) - 65
            count[idx] += 1
            maxf = max(maxf, count[idx])
            while right - left + 1 - maxf > k:
                count[ord(s[left]) - 65] -= 1
                left += 1
            best = max(best, right - left + 1)
        return best
