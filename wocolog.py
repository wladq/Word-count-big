# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 15:17:40 2026

@author: Wlad
"""

import logging 
logger = logging.getLogger(__name__)

def notfounderr():
    logging.error("Filename hasn't been provided")
    print("Please provide a filename in the argument.")
    
def permerr():
    logging.error("Permission to the file or path denied by the system.")
    print("Permission to the file or path denied by the system.")

def incorerr():
    logging.error("Incorrect filename or filename not found")
    print("File not found or incorrect. Please provide a correct filename or filename with a path. If the filename contains spacing, it should be quoted.")
