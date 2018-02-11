#!/usr/bin/python

import sys

# mapper for project

# input comes from STDIN (standard input)
def mapper():
    i = 0
    for line in sys.stdin:
        if i == 0:
            i += 1
            continue
        # remove leading and trailing whitespace
        i += 1
        line = line.strip()
        # split the line into words
        words = line.split(",")
        if len(words) == 22:
            words[2] = words[2][:4]
            print "{0}\t{1}\t{2}".format(words[0], words[2], words[7])
        
        
if __name__ == '__main__':
    mapper()
 
            

