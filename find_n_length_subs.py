#write and algorithm to return the most common n_size substring

def most_comm_subseq(input_string, n_size):
    lookup = {}
    max_index = len(input_string) - n_size
    idx = 0
    while idx <= max_index:
        if input_string[idx:idx+n_size] in lookup:
            lookup[input_string[idx:idx+n_size]]+=1
        else:
            lookup[input_string[idx:idx+n_size]]=1
        idx+=1
    return max(lookup, key=lambda k: lookup[k])

print most_comm_subseq('dogcatmousedog', 3)
