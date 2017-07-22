def firstNotRepeatingCharacter(s):
    """Find first unique character in string, cannot loop over string more than once"""
    
    count = {}
    
    for i, char in enumerate(s):
        if char not in count:
            count[char] = [i]
        else:
            count[char].append(i)
    
    first_unique = []
    
    for char, indexes in count.items():
        if len(indexes) < 2:
            first_unique.append((indexes[0], char))
            
    if not first_unique:
        return "_"
    
    
    first_unique.sort()
    return first_unique[0][1]
    