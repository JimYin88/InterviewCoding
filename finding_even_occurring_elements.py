'''
Created on Jun 2, 2022

@author: JimYi
'''

import collections

def even_times_integer(i_array):
    counter = collections.Counter(i_array)
    print(counter)
    return [item for item in counter if counter[item] % 2 == 0]
            
print(even_times_integer([1, 1, 2, 2, 3, 1, 3, 3, 4, 5, 6, 7, 7, 8, 8, 8]))
