'''
Created on Jun 3, 2022

@author: Jim Yin
'''

def single_element(arr):
    result = {}
    for element in arr:
        if element in result:
            result[element] = result[element] + 1
        else:
            result[element] = 1
    return [c for c in result if result[c] == 1]
                
print(single_element(['a', 'b', 'a', 'c', 'd', 'b', 'd', 'e']))
