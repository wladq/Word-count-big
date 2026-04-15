# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 16:56:18 2026

@author: Wlad
"""

import sys
import logging
import wocolog
import time
logger = logging.getLogger(__name__)
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s",
    datefmt="%d.%m.%y %H:%M:%S",
    filename="Info-logs.log")

start_tim = time.time()

def main() -> None:
    wocolog.starttimeinfo(start_tim)


def word_count(filepath):
    words=set()
    with open(filepath, 'r') as file:
        while True:
            subline = file.read(2048)
            if subline[-1].isspace:
                for word in subline.split():
                    words.add(word)
            elif subline is None:
                break
            else:
                subline.append(file.read(1))
                if subline[-1].isspace:
                    for word in subline.split():
                        words.add(word)

    wocolog.fileusedinfo(filepath)
    return len(words)


if __name__ == "__main__":
    try:
        numw = word_count(sys.argv[1])
        print(numw)
        wocolog.countednumberinfo(numw)
    except IndexError:
        wocolog.notfounderr()
    except PermissionError:
        wocolog.permerr()
    except FileNotFoundError:
        wocolog.incorerr()
    wocolog.endtimeanddurationinfo(start_tim, time.time())