"""
Find the most frequent integer in an array.
"""

import collections

def most_common_element(arr):
    collected = collections.Counter(arr)
    most_times = 0
    most_common = ''
    for item in collected:
        if collected[item] > most_times:
            most_common = item
            most_times = collected[item]
    return most_common

most_common_element([1, 2, 3, 1, 2, 1, 3, 1, 1, 4, 1, 6, 1, 7])
