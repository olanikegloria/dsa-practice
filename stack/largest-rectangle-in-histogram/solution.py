from typing import List

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        best = 0
        heights.append(0)
        for i, h in enumerate(heights):
            while stack and h < heights[stack[-1]]:
                idx = stack.pop()
                width = i if not stack else i - stack[-1] - 1
                best = max(best, heights[idx] * width)
            stack.append(i)
        heights.pop()
        return best
