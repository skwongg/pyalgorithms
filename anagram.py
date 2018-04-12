#Determine if 2 Strings are anagrams
# def check_if_anagram_or_nah(first_word, second_word):
#     if sorted(second_word) == sorted(first_word):
#         return True
#     else:
#         return False
#
# print(check_if_anagram_or_nah('racecar','raccear'))

def check_anagram(first_word, second_word):
    char_lookup = {}
    for letter in first_word:
        if letter not in char_lookup:
            char_lookup[letter] = 1
        else:
            char_lookup[letter]+=1

    for letter in second_word:
        if letter not in char_lookup:
            return False
        elif char_lookup[letter] == 1:
            char_lookup.pop(letter, None)
        else:
            char_lookup[letter]-=1
    if not char_lookup:
        return True
    else:
        return False
print(check_anagram('racecar','raccear'))
