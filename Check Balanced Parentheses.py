def is_balanced(expr):
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
