def is_uniquechar_word(word):
    charmap = {}
    for char in word:
        if char in charmap:
            return False
        else:
            charmap[char] = 1
    return True

print(is_uniquechar_word('abc'))
