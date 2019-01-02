def abbreviate(words):
    words_acronym = ("")
    separate_words = words.split(" ")
    for word in separate_words:
        words_acronym += word[0].upper()
    return words_acronym

print(abbreviate("I like big butts"))
