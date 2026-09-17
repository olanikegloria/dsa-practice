# Palindrome Number

**Topic:** arrays  
**Difficulty:** easy  
**LeetCode:** https://leetcode.com/problems/palindrome-number/

## Problem

Given an integer x, return true if x is a palindrome, and false otherwise.

## Approach

Half reversal

## Explanation

Reverse half the digits and compare to the other half.

## Complexity

- Time: O(log x)
- Space: O(1)

## Alternatives

String conversion.

## Common mistakes

Treating negative numbers as palindromes.

## Learning notes

Avoid string allocation for follow-up constraints.

## Solution

```python
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x != 0 and x % 10 == 0):
            return False
        rev = 0
        while x > rev:
            rev = rev * 10 + x % 10
            x //= 10
        return x == rev or x == rev // 10

```
