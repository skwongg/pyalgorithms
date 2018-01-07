class Schedule():
    def __init__(self):
        self.intervals = []
        self.endmax = 0
        self.startmax = 0

    def add(self, start, end):
        if not self.intervals:
            self.intervals.append([start, end])
        else:
            merge_left = None
            merge_right = None
            to_pop = []
            for i in range(len(self.intervals)):
                interstart = self.intervals[i][0]
                interend = self.intervals[i][1]
                if (start == interend):
                    merge_left = i
                elif (end == interstart):
                    merge_right = i

                if (start >= interstart) and (start <= interend):
                    self.intervals[i][1] = max(interend, end)
                elif (start <= interstart) and (end >= interend):
                    to_pop.append(i)
                elif (start < interstart) and (end < interstart):
                    self.intervals = self.intervals[:i] + [[start,end]] + self.intervals[i:]
                elif (start > interend) and (start > self.endmax):
                    self.intervals.append([start, end])

                self.startmax = max(self.startmax, start)
                self.endmax = max(self.endmax, end)

                if (merge_left != None) and (merge_right != None):
                    to_pop.append(merge_right)
                    self.intervals[merge_left] = [self.intervals[merge_left][0], self.intervals[merge_right][1]]

            for pair in reversed(to_pop):
                self.intervals.pop(pair)

        return self.intervals

    def remove(self, start, end):
        if not self.intervals:
            return self.intervals
        else:
            for i in range(len(self.intervals)):
                interstart = self.intervals[i][0]
                interend = self.intervals[i][1]
                if start > interend:
                    continue
                elif (start <= interstart) and (end > interstart) and (end < interend):
                    self.intervals[i][0] = end
                elif (start > interstart) and (end < interend):
                    self.intervals[i] = [end, interend]
                    self.intervals = self.intervals[:i] + [[interstart, start]] + self.intervals[i:]
                elif (start > interstart) and (start < interend) and (end > interend):
                    self.intervals[i] = [interstart, start]
            self.startmax = self.intervals[-1][0]
            self.endmax = self.intervals[-1][1]
            return self.intervals


""" Test cases """
a = Schedule()
assert(a.add(1,5) == [[1, 5]])
assert(a.remove(2,3) == [[1, 2], [3, 5]])
assert(a.add(6,8) == [[1, 2], [3, 5], [6, 8]])
assert(a.remove(4,7) == [[1, 2], [3, 4], [7, 8]])
assert(a.add(2,7) == [[1, 8]])
