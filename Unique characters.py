def unique_characters(astring):
    database = dict()
    for letter in astring:
        if letter not in database:
            database[letter] = 1
        else:
            return False
    return True
    
unique_characters('abcdefghijklmonopqrstuvwxx')
