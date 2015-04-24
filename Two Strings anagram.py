def anagrams_of_two_strings(string_1, string_2):
    d1 = {}
    for letter in string_1:
        if letter not in d1:
            d1[letter] = 1
        else:
            d1[letter] = d1[letter] + 1
    
    d2 = {}
    for letter in string_2:
        if letter not in d2:
            d2[letter] = 1
        else:
            d2[letter] = d2[letter] + 1
    
    if d1 == d2:
        return True
    else:
        return False
        
        
import collections

def anagrams_of_two_strings2(string_1, string_2):
    d1 = collections.Counter(string_1)
    d2 = collections.Counter(string_2)
    
    if d1 == d2:
        return True
    else:
        return False    
        
anagrams_of_two_strings('ababad', 'babada')
anagrams_of_two_strings2('ababad', 'babada')
        
anagrams_of_two_strings('ababad', 'babada')
