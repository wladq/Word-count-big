# -*- coding: utf-8 -*-
"""
Created on Mon Mar 30 17:00:20 2026

@author: Wlad
"""

import sys
import logging
import logging_helpers
import time 
logger = logging.getLogger(__name__)
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s",
    datefmt="%d.%m.%y %H:%M:%S",
    filename="Info-logs.log")

start_tim = time.time()
logging.info(f'Program started at {start_tim}')
def word_count(tekfil):
    words=set()
    with open(tekfil, 'r') as file:
        for line in file:
            for word in line.split():
                words.add(word) 
    logging.info(f"Words from {tekfil} will be counted")
    return (len(words))
    
    
            
            
if __name__ == "__main__":
    try:
        numw = word_count(sys.argv[1])
        print(numw)
        logging.info(f"Number of counted words: {numw}")
    except IndexError:
        logging_helpers.notfounderr()
    except PermissionError:
        logging_helpers.permerr()
    except FileNotFoundError:
        logging_helpers.incorerr()
logging.info(f'Program finished at {time.time()}')
logging.info(f'--- {(time.time() - start_tim)} seconds ---' )
