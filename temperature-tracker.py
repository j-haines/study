"""
Write a class TempTracker with these methods:

    - insert() — records a new temperature
    - get_max() — returns the highest temp we've seen so far
    - get_min() — returns the lowest temp we've seen so far
    - get_mean() — returns the mean ↴ of all temps we've seen so far
    - get_mode() — returns the mode ↴ of all temps we've seen so far

Optimize for space and time. Favor speeding up the getter functions (get_max(),
get_min(), get_mean(), and get_mode()) over speeding up the insert() function.

get_mean() should return a float, but the rest of the getter functions can 
return integers. Temperatures will all be inserted as integers. We'll record 
our temperatures in Fahrenheit, so we can assume they'll all be in the range 
0..110.

If there is more than one mode, return any of the modes.
"""
import collections


class TempTracker(object):
    def __init__(self):
        self.max_temp = 0
        self.min_temp = 0

        self.sum_temp = 0
        self.num_temps = 0
        self.mean = 0.0

        self.mode = 0
        self.max_occurences = 0
        self.occurences = collections.defaultdict(lambda: 0)


    def insert(self, temp):
        self.temps_buf.append(temp)
        self.max_temp = max(self.max_temp, temp)
        self.min_temp = min(self.min_temp, temp)

        self.sum_temp += temp
        self.num_temps += 1
        self.mean = self.sum_temp / self.num_temps

        self.occurences[temp] += 1
        if self.occurences[temp] > self.max_occurences:
            self.mode = temp
            self.max_temp = self.occurences[temp]

    def get_max(self):
        return self.max_temp

    def get_min(self):
        return self.min_temp

    def get_mean(self):
        return self.mean

    def get_mode(self):
        return self.mode
