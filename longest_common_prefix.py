def find_longest_prefix(words):
    """Given list of strings, find the longest common prefix"""

    longest = words[0]

    for word in words[1:]:
        for i in range(len(longest)):
            if i >= len(word):
                break

            if word[i] != longest[i]:
                longest = longest[:i]
                break

    return longest
