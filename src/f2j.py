#!/usr/local/bin/python2.7
# -*- coding: utf-8 -*-

import sys
import detecting_tools
import codecs
#import zhutils.word.pyjft.jft as jft

def run(file_name):

    in_ft = codecs.open("ft.txt", "r", "utf-8")
    str_ft = ""
    for line in in_ft:
        str_ft += line.strip("\n")
    in_ft.close()
    in_jt = codecs.open("jt.txt", "r", "utf-8")
    str_jt = ""
    for line in in_jt:
        str_jt += line.strip("\n")
    in_jt.close()

    in_file = codecs.open(file_name, "r", "utf-8")
    for line in in_file:
        words_raw = detecting_tools.uniform(line.strip("\n"))

        out_words = ""
        for uchar in words_raw:
            if detecting_tools.is_chinese(uchar):
                if str_ft.find(uchar) != -1:
                    out_words += str_jt[str_ft.find(uchar)].encode("utf8")
                else:
                    out_words += uchar.encode("utf8")
            else:
                out_words += uchar.encode("utf8")

        print out_words

    in_file.close()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print "cmd file"
        sys.exit(-1)
    file_name = sys.argv[1]
    run(file_name)
