'''
Created on Jun 2, 2022

@author: Jim Yin
'''

def unique_characters(astring):
    return len(set(astring)) == len(astring)
    
print(unique_characters('abcdefghijklmnopqrstuvwxx'))
print(unique_characters('abcdefghijklmnopqrstuvwx'))
