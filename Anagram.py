def is_anagram(word1, word2):
    word1 = list(word1.lower().replace(' ', ''))
    word2 = list(word2.lower().replace(' ', ''))

    word1.sort()
    word2.sort()

    if word1 == word2:
        anagram = True
    else:
        anagram = False
    print(anagram)
    return anagram


is_anagram('raska', 'R a K a S')
