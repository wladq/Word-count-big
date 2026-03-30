# -*- coding: utf-8 -*-
"""
Created on Mon Mar 30 17:00:20 2026

@author: Wlad
"""

import sys
import time 
start_time = time.time()

def word_count(tekfil):
    words=set()
    with open(tekfil, 'r') as file:
        for line in file:
            for word in line.split():
                words.add(word) 
    return (len(words))
            
            
if __name__ == "__main__":
    numw = word_count(sys.argv[1])
    print(numw)
print("--- %s seconds ---" % (time.time() - start_time))