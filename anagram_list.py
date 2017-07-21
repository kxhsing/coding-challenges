def make_list_anagrams(words):

    #corner case: empty list
    if not words:
        return []
    anagram_list = []

    #take each word and split to create indiv list of letters. then sort and join
    word_sorted_pairs = []

    for word in words:
        sorted_word = []
        for char in word:
            sorted_word.append(char)
        sorted_temp = sorted(sorted_word)
        joined_word = ''.join(sorted_temp)
        pair = (word, joined_word)
        word_sorted_pairs.append(pair)

    #create dict of sorted words as keys and list of variations of anagrams as values
    dict_sorted = {}
    for item in word_sorted_pairs:
        if item[1] not in dict_sorted:
            dict_sorted[item[1]] = [item[0]]
        else:
            dict_sorted[item[1]].append(item[0])

    for values in dict_sorted.itervalues():
        if len(values) > 1:
            anagram_list.append(values)

    return anagram_list
