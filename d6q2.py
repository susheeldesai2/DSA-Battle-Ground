"""Given a strings, return the length of the longest substring that contains at most two distinc characters.
Test Cases
Example 1:
Input: s = "eceba"
Output: 3
Explanation: The substring is "ece" which its length is 3.
Example 2:
Input: s = "ccaabbb"
Output: 5
Explanation: The substring is "aabbb" which its length is 5."""


def length_of_longest_substring_two_distinct(s: str) -> int:
    left = 0  
    char_count = {}  
    max_length = 0  

    for right in range(len(s)):  
        char_count[s[right]] = char_count.get(s[right], 0) + 1  
        
    
        # If we have more than 2 distinct characters, shrink window from the left
        while len(char_count) > 2:
            char_count[s[left]] -= 1  
            if char_count[s[left]] == 0:
                del char_count[s[left]]  
            left += 1  
        
        
        max_length = max(max_length, right - left + 1)

    return max_length
 
# Test cases
print(length_of_longest_substring_two_distinct("eceba"))  # Output: 3
print(length_of_longest_substring_two_distinct("bbbab"))  # Output: 5
print(length_of_longest_substring_two_distinct("ccaabbb"))  # Output: 5

