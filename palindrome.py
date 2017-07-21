def isPalindrome(s):
    """
    :type s: str
    :rtype: bool
    """
    together = []
    for char in s:
        if char.isalnum():
            together.append(char.lower())
    
    #print together
    together = ''.join(together)
    print together
    half = len(together)/2

    if len(together)%2 != 0: #tacocat
        if together[:half] == together[:half:-1]:
            return True
        else:
            return False
    elif len(together)%2 == 0:
        if together[:half] == together[:half-1:-1]:
            return True
        else:
            return False
    else:
        return False

def is_palindrome(word):
    index = len(word)/2
    if len(word) % 2!=0:
        if word[:index] == word[:index:-1]:
            return True
        else:
            return False
    elif len(word) % 2 == 0:
        if word[:index] == word[:index-1:-1]:
            return True
        else:
            return False
    else:
        return False

def removeWhite(s):
    new_word = []
    for char in s:
        if char.isalnum():
            new_word.append(char)
    s = ''.join(new_word)
    return s

def isPal(s):
    word = removeWhite(s)
    mid = len(word)/2
    if len(word) % 2==0:
        if word[:mid] == word[:mid-1:-1]:
            return True
    else:
        if word[:mid] == word[:mid:-1]:
            return True
    return False