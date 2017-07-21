def balanced_brackets_hash(phrase):
    """Better runtime than below solution, using dictionary"""
    pairs = {
        ')': '(',
        ']': '[',
        '}': '{',
        '>': '<'
    }
    store  = []

    for char in phrase:
        if char in pairs.values():
            store.append(char)
        if char in pairs:
            if not store:
                return False
            if store[-1] == pairs[char]:
                store.pop()
            else:
                return False
    if store:
        return False
    return True



def balanced_brackets(phrase):
    """Find if brackets are balanced with combo of diff types of brackets"""

    open_type = ['(', '{', '[', '<']
    closed_type = [')', '}', ']', '>']
    brackets = []
    for char in phrase:
        if char in open_type:
            brackets.append(char)
        elif char in closed_type:
            if not brackets:
                return False
            if open_type.index(brackets[-1]) == closed_type.index(char):
                brackets.pop()
            else:
                return False
    if not brackets:
        return True
    else:
        return False