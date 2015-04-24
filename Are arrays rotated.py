def is_rotated(alist, blist):
    if len(alist) != len(blist):
        return False
    for i in range(len(blist)):
        if alist[0] == blist[i]:
            blist_revised = blist[i:] + blist[:i]
            if alist == blist_revised:
                return True
    return False
    
is_rotated([1, 2, 3, 4, 5, 6, 7], [6, 7, 1, 2, 3, 4, 5])
