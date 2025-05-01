# LeetCode 3306 - Count of Substrings with Exactly K Consonants and All Vowels

## Problem Description

In this problem, you are given:
- A string `word` containing lowercase English letters
- An integer `k`

Your task is to count the number of substrings of `word` that:
1. Contain exactly `k` consonants (non-vowel characters)
2. Contain all five vowels ('a', 'e', 'i', 'o', 'u') at least once each

## Approach

The solution uses a sliding window approach with two pointers (`i` and `j`):

1. Initialize counters for vowels (using a dictionary) and consonants
2. Move the right pointer (`j`) to expand the window:
   - If the current character is a vowel, increment its count in the vowels dictionary
   - If it's a consonant, increment the consonant counter
3. If consonants exceed `k`, move the left pointer (`i`) to shrink the window until we have exactly `k` consonants
4. When we have exactly `k` consonants and all 5 vowels in our window:
   - Increment the result counter
   - Continue expanding the window with vowels (if possible) and updating the result
5. Return the final count of valid substrings

## Complexity Analysis

- Time Complexity: O(n), where n is the length of the input string
  - We traverse the string once with the two pointers
  - Each character is processed at most twice (once by each pointer)
  
- Space Complexity: O(1)
  - We use a dictionary to store vowel counts, but it will never have more than 5 entries
  - The rest of the variables use constant space

## Example

For the input string "iqeaouqi" with k = 2:
- The consonants are 'q' and 'q'
- All five vowels ('a', 'e', 'i', 'o', 'u') are present
- The valid substrings are multiple, and the function counts them correctly

## Note

This solution efficiently handles the constraint of having exactly `k` consonants while ensuring all vowels are present by maintaining a sliding window and appropriate counters.