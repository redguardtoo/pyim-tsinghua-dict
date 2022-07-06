#!/usr/bin/env python3
# -*- coding: utf-8-unix -*-

import argparse
import collections
import logging
logging.basicConfig(format='%(levelname)-7s :%(lineno)4d %(relativeCreated)9dms: %(message)s', datefmt='%H:%M:%S', level=logging.DEBUG)
logger = logging.getLogger(__name__)
debug = logger.debug   # debug('xx %s', v)
info = logger.info
error = logger.error


def get_words_line(pinyin, d):
    # debug("%s %s", pinyin, d)
    return "%s %s" % (pinyin, ' '.join(k for (k,c) in d.most_common()))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Generate .pyim')
    '''
    2 ways to restrict output:
    - pick top x words (by freq)
    - cut off words with DF lower (current way, easier to use?)
    '''
    parser.add_argument('df_threshold', type=int, nargs='?',
                        default=6000,
                        help='cut off DF lower')
    parser.add_argument('outfile', nargs='?', type=argparse.FileType('w'),
                        default=open("../pyim-tsinghua-dict.pyim", "wt")
                        )
    args = parser.parse_args()
    
    debug('%s', args)

    try:
        hanzi_items = [l.strip().split(",") for l in open("hanzi.csv", "r")]
        LEN_HANZI = len(hanzi_items)
        
        j = 0

        args.outfile.write(";; -*- coding: utf-8 -*--\n")
        
        same_sound_word2freq = collections.Counter()
        old_pinyin = ""
        for line in open("words-with-freq-sorted-by-pinyin.csv", "r"):
            a = line.strip().split(",")
            pinyin = a[0]
            word = a[1]
            freq = int(a[2])
            # to aid better choice of df_threshold
            # todo p2 random pick and output word close to threshold
            if freq < args.df_threshold:
                # skip
                continue

            if old_pinyin == pinyin:
                same_sound_word2freq[word] = max(same_sound_word2freq[word], freq)
            else:
                if len(same_sound_word2freq) > 0:
                    # if not the case of first line
                    args.outfile.write(get_words_line(old_pinyin, same_sound_word2freq))
                    args.outfile.write("\n")

                same_sound_word2freq.clear()
                same_sound_word2freq[word] = freq
                old_pinyin = pinyin

            pinyin1st = pinyin.split('-')[0]
            while(j < LEN_HANZI and hanzi_items[j][0] <= pinyin1st):
                args.outfile.write('%s %s\n' % (hanzi_items[j][0], hanzi_items[j][1]))
                j = j + 1
        debug(f'{j=} {LEN_HANZI=}')
        while(j < LEN_HANZI):
            args.outfile.write('%s %s\n' % (hanzi_items[j][0], hanzi_items[j][1]))
            j = j + 1

        args.outfile.write(get_words_line(pinyin, same_sound_word2freq))
        args.outfile.write("\n")
    except Exception as ex:
        logger.debug(ex, exc_info=1)
    finally:
        args.outfile.close()
