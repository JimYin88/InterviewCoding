def binary_search(arr, target):
    if len(arr) == 0:
        return False
    if len(arr) == 1:
        if arr[0] == target:
            return True
        else:
            return False
    
    mid_point = len(arr) // 2
        
    if arr[mid_point] == target:
        return True
    elif arr[mid_point] > target:
        return binary_search(arr[:mid_point], target)
    else:
        return binary_search(arr[mid_point+1:], target)
