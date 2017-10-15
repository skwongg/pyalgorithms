# Find the first non-repeated character in a String
def find_first_nonrepeating(stringput):
    charmap = {}
    ordered_chars = []
    for char in stringput:
        if char in charmap:
            charmap[char]+=1
        else:
            charmap[char]=1
            if char not in ordered_chars:
                ordered_chars.append(char)
    for char in ordered_chars:
        if charmap[char] == 1:
            return char
    return "No repeating chars found"
    
print (find_first_nonrepeating('zaaafuirhgaliunfsdlvdahyfwufiwahbfsavsdfsdf'))
