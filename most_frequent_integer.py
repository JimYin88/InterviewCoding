'''
Created on Jun 3, 2022

@author: Jim Yin
'''

import collections

def most_common_element(arr):
    collected = collections.Counter(arr)
    return [i for i in collected if collected[i] == max(collected[i] for i in collected)]

print(most_common_element([1, 2, 3, 1, 2, 1, 3, 1, 1, 4, 1, 6, 1, 7, 8, 8, 8, 8, 8, 8, 8]))
