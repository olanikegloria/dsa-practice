# Simplify Path

**Topic:** stack  
**Difficulty:** medium  
**LeetCode:** https://leetcode.com/problems/simplify-path/

## Problem

Given an absolute path for a Unix-style file system, transform it into its simplified canonical path.

## Approach

Stack

## Explanation

Stack pushes directory names; pop on ..; ignore . and empty.

## Complexity

- Time: O(n)
- Space: O(n)

## Alternatives

Manual index parsing.

## Common mistakes

Leaving stack non-empty after too many ..

## Learning notes

Unix path rules map cleanly to a stack.

## Solution

```python
class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        for part in path.split("/"):
            if part in ("", "."):
                continue
            if part == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(part)
        return "/" + "/".join(stack)

```
