def reverse_string(a_string):
    result = ""
    for letter in a_string:
        result = letter + result
    return result

reverse_string('abcdef')

def reverse_string2(a_string):
    if len(a_string) == 0:
        return
    else:
        return reverse_string2(a_string[1:]) + a_string[0]
    
reverse_string2('abcdef')
