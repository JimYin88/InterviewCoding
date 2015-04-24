import collections

def non_repeated_character(string):
    result = collections.Counter(string)
    for letter in string:
        if result[letter] == 1:
            print letter
            break
            
non_repeated_character('abababcddefc')
