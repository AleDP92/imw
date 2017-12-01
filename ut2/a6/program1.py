import sys


def count_words(phrase):
    summary = {}
    words = phrase.split()
    for i in words:
        if i in summary:
            summary[i] += 1
        else:
            summary[i] = 1
    return summary

phrase = sys.argv[1]
for word, count in (count_words(phrase).items()):
    print(word, ":", count)
