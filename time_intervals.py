"""

# Given a list of schedules, provide a list of times that are available
# for a meeting:

# Example input (busy times):
# [
#   [[4,5],[6,10],[12,14]],
#   [[4,9],[13,16]],
#   [[11,14]]
# ]

# Example Output (free times):
# [[0,4],[10,11],[16,24]]

"""

print "Hello"
# all_hours - set(busy_times) = free_times

#[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 2
# 2, 23, 24]

def find_the_mutually_avail_times(btimes):
    master_schedule = {}
    master_free_times = []
    for i in range(25):
        master_schedule[i] = False

    #btimes = list of available times of each person
#     hour_in_days=[i for i in range(25)]
    for btime in btimes:
        for interval in btime:
            for j in range(interval[0], interval[1]):
                master_schedule[j] = True
    last_idx = 0
    for master_i in range(25):
        if master_schedule[master_i] == False:
            continue
        else:
            master_free_times.append([last_idx, master_i])
            last_idx=master_i
    print master_free_times
            #second list item


#print (set(hour_in_days) - set(busy_times))
        #off by one check
        #create a list of times of availability
    #count_frequency on each individual time-slot (ie number of 1's)


examples=[
  [[4,5],[6,10],[12,14]],
  [[4,9],[13,16]],
  [[11,14]]
]

find_the_mutually_avail_times(examples)
