import string


def count_sentence():
    num = 0
    for ch in get:
        if ch in string.punctuation:
            num += 1
    return num


def count_word():
    two = 0
    for ch in get:
        if ch.isspace():
            two += 1
    return two


def count_letter():
    char = 0
    for ch in get:
        if ch.isalpha():
            char += 1
    return char


get = input("Text: ")

letters = count_letter()
words = count_word()
sentences = count_sentence()

super_letters = (letters / words) * 100
Super_sentences = (sentences / words) * 100
index = 0.0588 * super_letters - 0.296 * Super_sentences - 15.8

if index >= 14.343999999999998:
    print("Grade 16+")
elif index >= 8.133333333333333:
    print("Grade 10")
elif index >= 7.167272727272721:
    print("Grade 7")
elif index >= 6.504000000000001:
    print("Grade 9")
elif index < 6.504000000000001 and index > 3.5:
    print("Grade 8")
elif index >= 3.2799999999999976:
    print("Grade 2")
elif index >= 2.773090909090911:
    print("Grade 5")
elif index >= -0.061538461538463096 and index > -8.354285714285709:
    print("Grade 3")
elif index <= -8.354285714285709:
    print("Before Grade 1")

