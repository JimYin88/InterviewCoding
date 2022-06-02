'''
Created on Jun 3, 2022

@author: Jim Yin
'''

def common_elements(arr_a, arr_b):
    return set(arr_a).intersection(set(arr_b))
    
print(common_elements([1, 2, 3, 4, 5, 6, 7], [3, 5, 7, 9, 11, 13]))
