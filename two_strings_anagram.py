'''
Created on Jun 3, 2022

@author: Jim Yin
'''

def anagrams_of_two_strings(s1, s2):
    return sorted(s1) == sorted(s2)
        
import collections

def anagrams_of_two_strings2(s1, s2):
    d1 = collections.Counter(s1)
    d2 = collections.Counter(s2)
    
    return d1 == d2 
        
print(anagrams_of_two_strings('ababad', 'babada'))
print(anagrams_of_two_strings2('ababad', 'babada'))
        
print(anagrams_of_two_strings('abcabad', 'babada'))
