#given an alphanumeric number guaranteed to have:
    #1 integer paired to a sequence of characters
    #the integer is guaranteed to be 0-9
#output a string that represents character sequences multiplied by integer number of times

def multi_num_by_string(s):
    curr_num=0
    curr_chars=''
    output=''
    nums = set(['1','2','3','4','5','6','7','8','9','0'])

    for char in s:
        if char in nums:
            output+=curr_num*curr_chars
            curr_num=int(char)
            curr_chars=''
        else:
            curr_chars+=char
    output+=curr_num*curr_chars
    return output

print(multi_num_by_string('2a3bc4def'))
