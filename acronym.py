def abbreviate(words):
    words_acronym = ("")
    words = words.replace("-", " ")
    separate_words = words.split(" ")
    for word in separate_words:
        if word != "":
            words_acronym += word[0].upper()
    return words_acronym

print(abbreviate("I like    big butts"))
