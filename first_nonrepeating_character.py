'''
Created on Jun 3, 2022

@author: JimYi
'''
import collections

def non_repeated_character(string):
    result = collections.Counter(string)
    for letter in string:
        if result[letter] == 1:
            return letter
            
print(non_repeated_character('abababcddefc'))
