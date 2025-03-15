# Question 2: Filter Strings Based on Criteria
# You are given a list of strings and two integers k and m.
# Write a function that returns a new list containing only those strings that satisfy both of the following conditions:
# 1. The length of the string is greater than or equal to k.
# 2. The string contains at least m vowels (vowels are 'a', 'e', i', 'o', 'u').
# The output should maintain the original order of appearance in the input list.
# Function Input
# A list Ist of n strings.
# * An integer k representing the minimum length of strings to include.
# * An integer m representing the minimum number of vowels a string should have to be included.
# Test Cases
# Input: ["apple", "hi", "world", "yes", "python"], k= 4, m = 2
# Output: ["apple"]
# Input: ["education", "science", "art", "mathematics"], k = 5, m= 3 pass
# Output: ["education", "science", "mathematics"]
# Function Signature def filter strings(Ist: list(str, k: int, m: int) -> list[str]:


def filter_string(Ist: list[str], k: int, m: int) -> list[str]:
    """return a list of string with each word > k and contains least m vowels """

    vowels=['a', 'e', 'i', 'o', 'u']
    new_list=[]
    for word in Ist:
        count=0
        for letter in word:
            if letter in vowels:
                count+=1
        if count>=m and len(word)>=k:
            new_list.append(word)
    return new_list


str1=["apple", "hi", "world", "yes", "python"]
str2=["education", "science", "art", "mathematics"]
print(filter_string(str1, 4,2))
print(filter_string(str2, 5,3))