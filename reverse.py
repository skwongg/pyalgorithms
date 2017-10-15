# Reverse a String iteratively and recursively
def reverse_a_string_iteratively(stringput):
    char_bank = []
    for i, char in enumerate(stringput):
        char_bank.append(stringput[-i - 1])
    return ''.join(char_bank)
print (reverse_a_string_iteratively('someother iteratively'))

def reverse_a_string_recursively(stringput):
    if stringput=='':
        return stringput
    else:
        return reverse_a_string_recursively(stringput[1:]) + stringput[0]
print(reverse_a_string_recursively('show me recursively'))
