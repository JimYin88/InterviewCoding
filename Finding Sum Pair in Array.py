def array_pair(int_array, target):
    array = sorted(int_array)
    i, j = 0, len(array) - 1
    result = []
    while i < j:
        if array[i] + array[j] == target:
            result.append([array[i], array[j]])
            i += 1
        elif array[i] + array[j] > target:
            j -= 1
        else:
            i += 1
    return result
    
array_pair([1, 3, 6, 8, 9, 11, 13, 14, 15, 16, 18, 20, 23, 24, 26], 22)    
