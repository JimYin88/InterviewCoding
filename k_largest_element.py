'''
Created on Jun 3, 2022

@author: Jim Yin
'''

def k_largest_element(alist, k):
    alist.sort(reverse = True)
    return alist[k-1]
            
print(k_largest_element([1, 2, 3, 4, 4, 5, 6, 6, 7, 8, 9, 9, 10], 4))