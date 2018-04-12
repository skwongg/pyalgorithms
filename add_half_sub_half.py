#given an array of integers, add the first half and subtract the second half.
    #if length of array is odd, add the middle number

def add_half_sub_half(input_array):
    output=0
    for i, v in enumerate(input_array):
        if i < ((float(len(input_array)) / 2)):
            output+=v
        else:
            output-=v
    return output

input_arr = [1,1,2,2]
input_arr_odd = [1,1,2,2,2]
print(add_half_sub_half(input_arr)== -2)
print(add_half_sub_half(input_arr_odd)==0)
