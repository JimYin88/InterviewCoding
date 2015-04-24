def binary_search(alist, target):
    first = 0
    last = len(alist) - 1
    
    while first <= last:
        midpoint = (first + last) // 2
        if alist[midpoint] == target:
            return midpoint
        elif alist[midpoint] > target:
            last = midpoint - 1
        else:
            first = midpoint + 1
    
    return -1
    
binary_search([1, 2, 3, 5, 6, 7, 9, 11, 13, 17, 22], 8)
