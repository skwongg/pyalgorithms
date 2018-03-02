#Find the longest non-repeating character sequence.
#abcdefa would return abcdef

def longest_nonrepeating_substring(input_s):
    longest = ''
    longest_word = ''
    for char in input_s:
        if char in longest:
            cutoff = input_s.index(char) + 1
            longest_word = longest if len(longest) > len(longest_word) else longest_word
            longest = longest[cutoff:]
        longest+=char
    longest_word = longest if len(longest) > len(longest_word) else longest_word
    return longest_word

print(longest_nonrepeating_substring("abcdefa"))
