def isAnagram(self, s, t):
    """Are two strings anagrams of each other?"""
    
    s_count  = {}
    t_count = {}
    for char in s:
        s_count[char] = s_count.get(char, 0) +1
    
    for char in t:
        t_count[char] = t_count.get(char, 0) +1
    
    return t_count == s_count