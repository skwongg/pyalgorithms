
def is_palindrome(word):
    lengf = len(word)
    middle = (int(lengf/2))
    left_half = word[0:middle]
    right_half = word[middle:]
    for i in range(0, int(len(word)/2)):
        if word[i] == word[-1 - i]:
            continue
        else:
            return False
    return True
print (is_palindrome('badab'))
