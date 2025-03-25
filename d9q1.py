#Day9Q17: Longest uncommon sub sequence
from typing import List

def subsequence(s1,s2):
    i = 0
    for char in s2:
        if i < len(s1) and s1[i] == char:
            i += 1
    return i == len(s1)

def findLUSlength(strs):
    strs.sort(key=len, reverse=True)  # Sort by descending length
    
    for i, s in enumerate(strs):
        uncommon = True
        for j, t in enumerate(strs):
            if i != j and subsequence(s, t):  # Check if s is a subsequence of t
                uncommon = False
                break
        if uncommon:
            return len(s)
    
    return -1


print(findLUSlength(["aba", "cdc", "eae"])) 
print(findLUSlength(["aaa", "aaa", "aa"]))  