#Determine if 2 Strings are anagrams
def check_if_anagram_or_nah(first_word, second_word):
    if sorted(second_word) == sorted(first_word):
        return True
    else:
        return False
        
print(check_if_anagram_or_nah('racecar','raccear'))
