def k_largest_element(alist, k):
    
    counted = dict()
    
    for i in alist:
        if i in counted:
            counted[i] = counted[i] + 1
        else:
            counted[i] = 1
            
    counted = sorted(counted.items(), reverse = True)
        
    high_count = 0
    for j in counted:
        high_count += j[1]
        if high_count >= k:
            print j[0]
            break
            
k_largest_element([1, 2, 3, 4, 4, 5, 6, 6, 7, 8, 9, 9, 10], 4)
