# Created on Jun 9, 2022
#
# @author: Jim Yin


def is_balanced(expr):
    """
    Check whether an expression has balanced (), [], {}
    """
    if len(expr) % 2 != 0:
        return False
    matching_pair = {')': '(', ']': '[', '}': '{'}
    stack = []
    for item in expr:
        if item in '([{':
            stack.append(item)
        else:
            last = stack.pop()
            if last != matching_pair[item]:
                return False
    if len(stack) == 0:
        return True
    else:
        return False
        
        
is_balanced('(){}[]()')
