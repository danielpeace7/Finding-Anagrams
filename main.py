# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagram(word1, word2):

    # [assignment] Add your code here

    if (sorted(word1) == sorted(word2)):

        return True

    else:

        return False

word1 ="state"

word2 ="taste"

print(find_anagram(word1, word2))