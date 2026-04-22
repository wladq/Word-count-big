# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 16:56:18 2026

@author: Wlad
"""

import argparse
import logging
import logging_helpers
from pathlib import Path 
import time
#import sys


logger = logging.getLogger(__name__)
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s",
    datefmt="%d.%m.%y %H:%M:%S",
    filename="Info-logs.log")

start_tim = time.time()

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

    logging_helpers.fileusedinfo(filepath)
    return len(words)

def main() -> None:
    parser = argparse.ArgumentParser(
        description="Count unique words in a file."
    )
    parser.add_argument(
        "filepath",
        type=Path,
        help="Path to the input text file"
    )
    args = parser.parse_args()
    start_time = time.time()
    logging_helpers.startTimeInfo(start_time)
    try:
        wordCount = word_count(args.filepath)
        print(wordCount)
        logging_helpers.countedNumberInfo(wordCount)
    except IndexError:
        logging_helpers.notFoundError()
    except PermissionError:
        logging_helpers.logPermissionError()
    except FileNotFoundError:
        logging_helpers.logIncorrectError()
    logging_helpers.endTimeAndDurationInfo(start_time, time.time())

if __name__ == "__main__":
    main()