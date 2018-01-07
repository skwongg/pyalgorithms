

def longest_substring(word1, word2):
    longest = ''
    curr = ''
    for idx in range(len(word1)):
        if curr + word1[idx] in word2:
            curr+=word1[idx]
            if len(curr) > len(longest):
                longest = curr
    return longest

print longest_substring('fjdslf', 'askfjdslfadjlfasabc')
