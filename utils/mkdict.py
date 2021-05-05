#!/usr/bin/env python
def is_unique(items, item):
    for i in items:
        if(i[1] == item[1]):
            return False
    return True


def filter_word_list(word_list):
    if (len(word_list) <= 1):
        return word_list
    result = []
    items = sorted(word_list, key=lambda a: a[1])
    for item in items:
        if(len(result) == 0):
            result.append(item)
        elif is_unique(result, item):
            result.append(item)

    # sort by freq this time
    return sorted(result, key=lambda a: a[2], reverse=True)


def print_words(word_list_same_sound):
    if len(word_list_same_sound) > 0:
        items = filter_word_list(word_list_same_sound)

        # # ouput csv with unique words
        # for item in items:
        #     print('%s,%s,%s' % (item[0],item[1],item[2]))

        # output pyim dictionary
        print("%s %s" % (items[0][0], ' '.join(map(lambda a: a[1], items))))

if __name__ == "__main__":
    hanzi_items = []
    for l in open("hanzi.csv", "r").readlines():
        hanzi_items.append(l.strip().split(","))

    j = 0

    lines = open("words-with-freq-sorted-by-pinyin.csv", "r").readlines()
    word_list_same_sound = []
    old_pinyin = ""

    print(";; -*- coding: utf-8 -*--")
    for index, line in enumerate(lines):
        a = line.strip().split(",")
        pinyin = a[0]
        word = a[1]
        freq = a[2]

        if old_pinyin == pinyin:
            word_list_same_sound.append((pinyin, word, int(freq)))
        else:
            print_words(word_list_same_sound)

            word_list_same_sound = []
            word_list_same_sound.append((pinyin, word, int(freq)))
            old_pinyin = pinyin

        while(j < len(hanzi_items) and hanzi_items[j][0] <= pinyin.split('-')[0]):
            print('%s %s' % (hanzi_items[j][0], hanzi_items[j][1]))
            j = j + 1

    print_words(word_list_same_sound)
