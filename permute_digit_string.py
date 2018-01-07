#Given a digit string, return all possible letter combinations that the number could represent
#Mapping of digit to letters just liek telephone buttons
#number of characters for output should be equal to input
#Input: Digit string "23"
#Ouytput: ['ad', 'ae', 'af','bd','be','bf','cd','ce','cf']



def permute_digit_string(num_s):
    keypad_lookup = {   '2':'abc',
                        '3':'def',
                        '4':'ghi',
                        '5':'jkl',
                        '6':'mno',
                        '7':'pqrs',
                        '8':'tuv',
                        '9':'wxyz'}
    combo_bank = ['']

    for char in num_s:
        if char in keypad_lookup:
            temp_bank = []
            for lett in keypad_lookup[char]:
                for thing in combo_bank:
                    temp_bank.append('{0}{1}'.format(thing, lett))
            combo_bank = temp_bank
        else:
            continue
    return combo_bank

print permute_digit_string('2345')
assert permute_digit_string('23') == ['ad', 'ae', 'af','bd','be','bf','cd','ce','cf']
