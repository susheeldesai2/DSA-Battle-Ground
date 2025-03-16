# Question 3: Length of Last Word
# You are given a sentence s that contains words and spaces. Your task is to find the length of the las word in the sentence.
# Note:
# * A word is a group of letters without spaces.
# * The sentence may have extra spaces at the beginning, middle, or end.
# * You need to ignore the spaces and focus only on words.

def Lenof_lastword(s: str) -> int:
    word=s.split()
    return len(word[-1])

print(Lenof_lastword("my name is Susheel    ")) #7
print(Lenof_lastword("     the world is round ")) #5
print(Lenof_lastword("How you doin")) #4

