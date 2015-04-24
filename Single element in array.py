"""
Find the only element in an array that only occurs once.
"""

def single_element(arr):
    result = {}
    for element in arr:
        if element in result:
            result[element] = result[element] + 1
        else:
            result[element] = 1
    for count in result:
        if result[count] == 1:
            print count
            
single_element(['a', 'b', 'a', 'c', 'd', 'b', 'd'])
