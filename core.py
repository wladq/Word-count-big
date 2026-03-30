# -*- coding: utf-8 -*-
"""
Created on Sat Mar  7 15:50:01 2026

@author: Wlad
"""


import time 
start_time = time.time()
#print("Enter file name with path")
#tekfil=input()
tekfil="nowy 1.txt"
print(f"Words from {tekfil} will be counted")

with open(tekfil, 'r') as file:
    zawar = file.read()
    
print(zawar)

casedown = [i.lower() for i in (zawar.replace(".","").split())]
print(f"Total number of words: {len(casedown)}")
print(f"Number of unique words: {len(set(casedown))}")
print("--- %s seconds ---" % (time.time() - start_time))