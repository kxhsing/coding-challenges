def is_matched(expression):
    brackets = []
    bracket_pairs = {')':'(', ']':'[', '}':'{'}
    openers = set(bracket_pairs.itervalues())

    for char in expression:
        if char in openers:
            brackets.append(char)
        else:
            closing = bracket_pairs[char]
            if brackets[-1] != closing:
                return False
            else:
                brackets.pop()
    return True