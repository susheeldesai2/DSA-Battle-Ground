
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
