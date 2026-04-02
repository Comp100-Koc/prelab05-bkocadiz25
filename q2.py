def remove_adjacent_duplicates(s):
    '''
    Given a string remove all the adjacent duplicate characters and return the string
    '''
    result = ""
    
    for char in s:
        if result and result[-1] == char:
            result = result[:-1]
        else:
            result += char
    
    return result