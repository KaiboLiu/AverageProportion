'''
10/17/2018 Wed
__author__: Kaibo Liu
calculate the AL for baseline (full sentence)
according to the definition of AL, full sentence tranlation should have AL=|x|, so the overall AL is the mean length of source(not corpus level average weighted on tgt length)
'''
import sys
import matplotlib.pyplot as plt
import matplotlib.colors as colors
import numpy as np

def AL_gold(f1, f2):
    srcs = open(f1, 'r').readlines()
    n = len(srcs)
    length = sum(len(src.strip().split()) for src in srcs)
    return length/n

if __name__=="__main__":
    if len(sys.argv) == 3:
        f1 = sys.argv[1]
        f2 = sys.argv[2]
    else:
        f1 = 'dev_06.zh.bpe'
        f2 = 'dev_06.en.0.bpe'
    print('{} -> {}\n{}'.format(f1, f2, AL_gold(f1, f2)))
