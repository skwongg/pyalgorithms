def most_comm_subseq(input_string, n_size):
    combo_store ={}
    for i, subs in enumerate(input_string):
        if (i+n_size) < len(input_string) + 1:
            if input_string[i: i+n_size] not in combo_store:
                combo_store[input_string[i: i+n_size]]=1
            else:
                combo_store[input_string[i: i+n_size]]+=1
    highest = max(combo_store.values())
    all_highest = [k for k, v in combo_store.items() if v == highest]

    earliest_index=None
    earliest_word=''
    if len(all_highest) == 1:
        return all_highest[0]

    for one_high in all_highest:
        if input_string.index(one_high) < earliest_index or earliest_index==None:
            earliest_index = input_string.index(one_high)
            earliest_word = one_high
        else:
            continue
    return earliest_word

print most_comm_subseq('dogcatmouse', 3)
