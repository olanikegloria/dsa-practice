# Encode and Decode Strings

**Topic:** arrays  
**Difficulty:** medium  
**LeetCode:** https://leetcode.com/problems/encode-and-decode-strings/

## Problem

Design an algorithm to encode a list of strings to a string. The encoded string is then sent over the network and is decoded back to the original list of strings. Implement encode and decode.

## Approach

Length-prefixed encoding

## Explanation

Prefix each string with its length and a delimiter so empty strings and hashes inside the payload stay unambiguous.

## Complexity

- Time: O(n)
- Space: O(n)

## Alternatives

A non-appearing separator, which fails once that character shows up in a word.

## Common mistakes

Splitting on a delimiter without a length, which breaks on the delimiter itself.

## Learning notes

The length tells you exactly where the next record starts.

## Solution

```python
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

```
