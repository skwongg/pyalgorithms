#Find pairs in an integer array whose sum is equal to 10

def make_ordered_pair(pair):
    if pair[0] <= pair[1]:
        return [pair[0], pair[1]]
    else:
        return [pair[1], pair[0]]

def find_pairs_equaling_target_num(num_inputs, target_num):
    pair_collector=[]
    for i, num in enumerate(num_inputs):
        for inner_num in num_inputs[i:]:
            sorted_nums = make_ordered_pair([num, inner_num])
            if num + inner_num == target_num and (sorted_nums not in pair_collector):
                pair_collector.append([num, inner_num])
    return pair_collector if pair_collector else "No pairs found."

print(find_pairs_equaling_target_num([1,2,3,4,5,6,7,8,10,5,2,8], 10))
