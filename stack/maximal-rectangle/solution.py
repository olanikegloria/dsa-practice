from typing import List

class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        cols = len(matrix[0])
        heights = [0] * cols
        best = 0
        for row in matrix:
            for c in range(cols):
                heights[c] = heights[c] + 1 if row[c] == "1" else 0
            best = max(best, self.largestRectangleArea(heights))
        return best

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
