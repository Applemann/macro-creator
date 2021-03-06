#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""

  Copyright (c) 2016-2017 Martin Jablecnik
  Authors: Martin Jablecnik
  Description: Config file
  
"""
import os, sys
from os.path import expanduser

DEVEL=False

if DEVEL:
    # Development
    SCRIPT_PATH = os.path.dirname(sys.argv[0])
    OUTPUT_PATH = SCRIPT_PATH + '/tmp/macros/'
    RAW_PATH = SCRIPT_PATH + '/tmp/raw-data/'
    VERBOSE = True

else:
    # Production
    OUTPUT_PATH = expanduser("~")+'/.config/macronaut/macros/'
    RAW_PATH = expanduser("~")+'/.config/macronaut/raw-data/'
    VERBOSE = False


