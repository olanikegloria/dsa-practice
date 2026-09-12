# Isomorphic Strings

**Topic:** hash-maps  
**Difficulty:** easy  
**LeetCode:** https://leetcode.com/problems/isomorphic-strings/

## Problem

Given two strings s and t, determine if they are isomorphic. Two strings s and t are isomorphic if the characters in s can be replaced to get t.

## Approach

Two hash maps / mapping check

## Explanation

Bijective char mapping must be one-to-one both ways.

## Complexity

- Time: O(n)
- Space: O(alphabet)

## Alternatives

Index mapping arrays.

## Common mistakes

Allowing two chars to map to same target.

## Learning notes

Isomorphism requires consistent unique mapping.

## Solution

```python
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

```
