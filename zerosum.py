#
# Input: {4, 2, -3, 1, 6}
# Output: true
# Input: {4, 2, 0, 1, 6}
# Output: true
# Input: {-3, 2, 3, 1, 6}
# Output: false

#given a list return true if zero sum is achievable with any of the elements from the list
#return false if not achievable


def zerosum(inputlist):
    seen_nums = []
    curr_collect = []
    curr_counter= 0
    for i, num in enumerate(inputlist):
        if num + curr_counter == 0:
            return True
        else:
            curr_collect.append(num)
            print curr_collect
            print i
            print "*" * 100
            #collect from [-i:-1]
            # seen_nums.append(curr_last_num + num)
                # seen_nums.append(num + inputlist[i-1])


    # print curr_collect

zerosum([4,2,-3,1,6, 9])
