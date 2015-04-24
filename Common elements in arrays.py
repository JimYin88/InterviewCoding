def common_elements_in_arrays(arr_a, arr_b):
    arr_a = set(arr_a)
    arr_b = set(arr_b)
    result = arr_a.intersection(arr_b)
    print result
    
common_elements_in_arrays([1, 2, 3, 4, 5, 6, 7], [3, 5, 7, 9, 11, 13])
