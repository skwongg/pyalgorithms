#Find the most frequent integer in an array
def most_frequent_int(data):
    num_counter = {}
    most_common = None
    max_count = 0
    for d in data:
        if d in num_counter:
            num_counter[d]+=1
        else:
            num_counter[d]=1
    for k, v in num_counter.items():
        if num_counter[k] > max_count:
            most_common = v
    return most_common

print (most_frequent_int([1,1,2,3,4,5,1,1,1,1,1,1,5,1,231,31,3123,123,1]))
