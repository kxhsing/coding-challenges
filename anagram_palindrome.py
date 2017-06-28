def is_anagram_palindrome(word):
    letters = {}
    for char in word:
        if char in letters:
            letters[char] +=1
        else:
            letters[char] = 1

    print letters

    even_odd = {'even':0, 'odd':0}

    for letter, count in letters.iteritems():
        if count % 2==0:
            even_odd['even']+=1
        else:
            even_odd['odd']+=1

    print even_odd

    if even_odd['odd'] > 1:
        return False
    else:
        return True

is_anagram_palindrome('tacocat')
is_anagram_palindrome('toot')
is_anagram_palindrome('nope')