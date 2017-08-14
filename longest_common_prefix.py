def find_longest_prefix(words):
    """Given list of strings, find the longest common prefix"""

    if not words:
        return ""

    longest = words[0]

    for word in words[1:]:
        if not word:
            return ""
            
        for i in range(len(longest)):
            if i >= len(word):
                longest = longest[:i]
                break

            if word[i] != longest[i]:
                longest = longest[:i]
                break

    return longest
