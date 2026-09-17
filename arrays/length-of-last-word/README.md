# Length of Last Word

**Topic:** arrays  
**Difficulty:** easy  
**LeetCode:** https://leetcode.com/problems/length-of-last-word/

## Problem

Given a string s consisting of words and spaces, return the length of the last word in the string.

## Approach

Reverse scan

## Explanation

Scan from the end; skip trailing spaces then count word chars.

## Complexity

- Time: O(n)
- Space: O(1)

## Alternatives

split() and take last token.

## Common mistakes

Not trimming trailing spaces first.

## Learning notes

Two-pointer from end avoids extra strings.

## Solution

```python
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        i = len(s) - 1
        while i >= 0 and s[i] == " ":
            i -= 1
        length = 0
        while i >= 0 and s[i] != " ":
            length += 1
            i -= 1
        return length

```
