# Find the first non-repeated character in a String

def find_first_nonrepeating(stringput):
    possible = []
    not_possible = set()
    for char in stringput:
        if (char not in possible) and (char not in not_possible):
            possible.append(char)
        elif (char in possible):
            possible.remove(char)
            not_possible.add(char)
        else:
            not_possible.add(char)
    return possible[0] if char else []


print (find_first_nonrepeating('aaafuihgagliunnfsdlvdahyyfwufiwahbfsavsdfsdf'))
