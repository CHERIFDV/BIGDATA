#!/usr/bin/env python

import sys
wordList = dict()
# input comes from STDIN (standard input)
for line in sys.stdin:
    line = line.strip()
    
    words = line.split('|')

    print '%s\t%s' % (words[5],words[2])
