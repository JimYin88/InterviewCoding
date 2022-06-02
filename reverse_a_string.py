'''
Created on Jun 2, 2022

@author: Jim Yin
'''

def reverse_string(a_string):
    result = ""
    for letter in a_string:
        result = letter + result
    return result

reverse_string('abcdef')

def reverse_string2(a_string):
    return a_string[::-1]
    
print(reverse_string2('abcdefg'))
